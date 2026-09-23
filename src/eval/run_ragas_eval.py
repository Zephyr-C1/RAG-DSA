import json
import logging
from pathlib import Path
from typing import List, Dict, Any
from src.retrieval.engine import HybridRetriever
from src.orchestration.pipeline import DecisionPipeline

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def evaluate_benchmark(benchmark_path: str = "data/benchmark/qa_dataset.json", top_k: int = 4):
    benchmark_file = Path(benchmark_path)
    if not benchmark_file.exists():
        logger.error(f"Benchmark file not found: {benchmark_path}")
        return

    with open(benchmark_file, "r", encoding="utf-8") as f:
        qa_dataset: List[Dict[str, str]] = json.load(f)

    logger.info("Initializing local retriever and LLaMA-3.1 decision engine...")
    retriever = HybridRetriever()
    pipeline = DecisionPipeline(retriever=retriever)

    eval_results = []
    print(f"\n==================== Starting Benchmark Evaluation ({len(qa_dataset)} items) ====================")

    for i, item in enumerate(qa_dataset, start=1):
        question = item["question"]
        ground_truth = item["ground_truth"]
        print(f"\n[Test Item {i}/{len(qa_dataset)}]")
        print(f"Query: {question}")

        result = pipeline.execute(query=question, top_k=top_k)
        cod_trace = result.get("cod_trace", {})
        assessment = cod_trace.get("assessment", "")
        recommendation = cod_trace.get("recommendation", "")
        full_text = f"{assessment} {recommendation}"

        retrieved_sources = [
            f"{n['metadata'].get('source', '')} p.{n['metadata'].get('page', 0)}"
            for n in result.get("retrieved_nodes", [])
        ]

        print(f"Retrieved Sources: {retrieved_sources}")
        print(f"Assessment Snippet: {assessment[:180]}...")
        print(f"Confidence: {cod_trace.get('confidence', 'N/A')}")

        keywords = [w.strip(".,()") for w in ground_truth.split() if len(w) > 4 and w.isalnum()]
        hit_count = sum(1 for kw in keywords if kw.lower() in full_text.lower())
        hit_ratio = hit_count / max(len(keywords), 1)

        eval_results.append({
            "id": i,
            "question": question,
            "ground_truth": ground_truth,
            "cod_trace": cod_trace,
            "retrieved_sources": retrieved_sources,
            "keyword_hit_ratio": round(hit_ratio, 3)
        })

    output_path = Path("data/benchmark/eval_results.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(eval_results, f, ensure_ascii=False, indent=2)

    avg_score = sum(r["keyword_hit_ratio"] for r in eval_results) / len(eval_results)
    print("\n==================== Evaluation Summary ====================")
    print(f"Total benchmark queries: {len(eval_results)}")
    print(f"Average compliance keyword hit ratio: {avg_score * 100:.1f}%")
    print(f"Evaluation report saved to: {output_path}")

if __name__ == "__main__":
    evaluate_benchmark()