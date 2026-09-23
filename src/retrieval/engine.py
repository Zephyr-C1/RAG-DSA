import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional
import requests
import faiss
import numpy as np
import torch
from sentence_transformers import SentenceTransformer, CrossEncoder
from rank_bm25 import BM25Okapi

logger = logging.getLogger(__name__)

INDEX_DIR = Path("data/index")
FAISS_FILE = INDEX_DIR / "faiss_index.bin"
DOCSTORE_FILE = INDEX_DIR / "docstore.json"

EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"
RERANKER_MODEL_NAME = "BAAI/bge-reranker-large"
OLLAMA_API_URL = "http://localhost:11434/api/generate"

class HyDEGenerator:
    """
    Generates a brief hypothetical regulatory clause passage using the local LLM.
    Bridging the gap between interrogative user queries and regulatory declarative statements.
    """
    def __init__(self, model_name: str = "llama3.1:8b-instruct-q8_0"):
        self.model_name = model_name

    def generate_hypothetical_passage(self, query: str) -> str:
        prompt = (
            f"You are drafting a technical clause for the Cyprus Transmission Grid Code.\n"
            f"Write a brief, direct, declarative regulatory statement answering the following operational query.\n"
            f"Query: {query}\n"
            f"Declarative Clause Statement (do not include greetings or explanations, output 1-2 formal sentences only):"
        )
        try:
            res = requests.post(
                OLLAMA_API_URL,
                json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"temperature": 0.1, "num_ctx": 2048, "num_predict": 120}
                },
                timeout=15
            )
            if res.status_code == 200:
                hypo_text = res.json().get("response", "").strip()
                if hypo_text:
                    logger.info(f"HyDE Document generated: {hypo_text[:120]}...")
                    return hypo_text
        except Exception as e:
            logger.warning(f"HyDE generation skipped due to connection or timeout: {e}")
        return query


class HybridRetriever:
    """
    Two-Phase Advanced Retrieval Architecture:
    - Pre-Retrieval: HyDE (Hypothetical Document Embeddings) via local LLaMA-3.1
    - Phase 1: Hybrid Retrieval (FAISS Dense Vector Search + BM25 Sparse Keyword Search)
    - Phase 2: High-Capacity Cross-Encoder Neural Reranking (BAAI/bge-reranker-large)
    """
    def __init__(self, use_reranker: bool = True, use_hyde: bool = True):
        logger.info("Initializing HybridRetriever with BGE-Reranker-Large and HyDE...")
        self.use_reranker = use_reranker
        self.use_hyde = use_hyde

        if not FAISS_FILE.exists() or not DOCSTORE_FILE.exists():
            raise FileNotFoundError(f"Index files missing at {INDEX_DIR}. Please run scripts/update_knowledge_base.sh first.")

        with open(DOCSTORE_FILE, "r", encoding="utf-8") as f:
            self.docs: List[Dict[str, Any]] = json.load(f)

        self.index = faiss.read_index(str(FAISS_FILE))
        logger.info(f"Loaded {len(self.docs)} documents from {DOCSTORE_FILE}")

        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.embed_model = SentenceTransformer(EMBEDDING_MODEL_NAME, device=device)

        tokenized_corpus = [doc["content"].lower().split() for doc in self.docs]
        self.bm25 = BM25Okapi(tokenized_corpus)

        if self.use_reranker:
            logger.info(f"Loading Phase-2 Heavy Reranker: {RERANKER_MODEL_NAME} on {device}...")
            self.reranker = CrossEncoder(
                RERANKER_MODEL_NAME,
                device=device,
                automodel_args={"torch_dtype": torch.float16} if device == "cuda" else {}
            )
        else:
            self.reranker = None

        if self.use_hyde:
            self.hyde = HyDEGenerator()
        else:
            self.hyde = None

    def retrieve(self, query: str, top_k: int = 4, candidate_pool_size: int = 60) -> List[Dict[str, Any]]:
        # 1. HyDE 假想文档生成（对齐法规陈述文风）
        search_document = query
        if self.use_hyde and self.hyde:
            search_document = self.hyde.generate_hypothetical_passage(query)

        # 2. Phase 1: Dense FAISS 检索（以假想陈述向量比对知识库切片）
        bge_prompt = f"Represent this sentence for searching relevant passages: {search_document}"
        query_emb = self.embed_model.encode([bge_prompt], normalize_embeddings=True)
        query_emb = np.array(query_emb).astype("float32")
        
        pool_k = min(candidate_pool_size, len(self.docs))
        dense_scores, dense_indices = self.index.search(query_emb, pool_k)

        dense_candidates = {}
        for score, idx in zip(dense_scores[0], dense_indices[0]):
            if idx != -1:
                dense_candidates[idx] = float(score)

        # 3. Phase 1: Sparse BM25 检索（融合原始提问与假想陈述的关键词）
        combined_keywords = f"{query} {search_document}".lower().split()
        bm25_scores = self.bm25.get_scores(combined_keywords)
        bm25_indices = np.argsort(bm25_scores)[::-1][:pool_k]

        sparse_candidates = {}
        for idx in bm25_indices:
            sparse_candidates[idx] = float(bm25_scores[idx])

        # 4. 合并候选池
        all_candidate_indices = list(set(list(dense_candidates.keys()) + list(sparse_candidates.keys())))
        candidate_docs = [self.docs[i] for i in all_candidate_indices]

        # 5. Phase 2: Neural Cross-Encoder (Large) 深度重排
        if self.use_reranker and self.reranker and candidate_docs:
            # 原始用户提问直接与候选切片全文进行多头交叉注意力精排
            pairs = [[query, doc["content"]] for doc in candidate_docs]
            rerank_scores = self.reranker.predict(pairs)

            for doc, score in zip(candidate_docs, rerank_scores):
                doc["rerank_score"] = float(score)

            candidate_docs.sort(key=lambda x: x.get("rerank_score", 0.0), reverse=True)
            return candidate_docs[:top_k]
        else:
            candidate_docs.sort(key=lambda x: dense_candidates.get(self.docs.index(x), 0.0), reverse=True)
            return candidate_docs[:top_k]

# Backward compatibility alias
PowerGridRetriever = HybridRetriever

if __name__ == "__main__":
    retriever = HybridRetriever()
    test_q = "What is the maximum allowable RoCoF that generating units must withstand without disconnecting?"
    results = retriever.retrieve(test_q, top_k=3)
    print(f"\n--- Top Retrieved Results for: {test_q} ---")
    for idx, r in enumerate(results, start=1):
        print(f"[{idx}] Page {r['metadata'].get('page')} | Clause {r['metadata'].get('section')} | Rerank Score: {r.get('rerank_score', 0):.4f}")
        print(f"Content: {r['content'][:150]}...\n")