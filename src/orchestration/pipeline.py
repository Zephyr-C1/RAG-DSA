import json
import logging
import uuid
import requests
from typing import Dict, Any, List, Optional
from src.retrieval.engine import HybridRetriever
from src.orchestration.cod_schema import DecisionAnalysisOutput, CodeEvidenceItem
from src.orchestration.simulation_tool import run_contingency_simulation

logger = logging.getLogger(__name__)

class LocalOllamaClient:
    """Local Ollama LLM client for offline inference with robust timeout settings."""
    def __init__(self, model_name: str = "llama3.1:8b-instruct-q8_0", base_url: str = "http://localhost:11434"):
        self.model_name = model_name
        self.generate_url = f"{base_url}/api/generate"
        self.keep_alive = "2h"

    def generate(self, prompt: str, system_prompt: Optional[str] = None, format_json: bool = False) -> str:
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "keep_alive": self.keep_alive,
            "options": {
                "temperature": 0.0,
                "num_ctx": 8192
            }
        }
        if system_prompt:
            payload["system"] = system_prompt
        if format_json:
            payload["format"] = "json"

        try:
            # 将超时时间从 120 秒提升到 300 秒，防止复杂长推理被主动掐断
            response = requests.post(self.generate_url, json=payload, timeout=300)
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.exceptions.Timeout:
            logger.error("Local Ollama inference timed out (exceeded 300s limit).")
            raise RuntimeError("Ollama inference timed out after 300 seconds. Check GPU compute load.")
        except requests.exceptions.RequestException as e:
            logger.error(f"Local Ollama inference failed: {e}")
            raise RuntimeError(f"Unable to connect to Ollama backend ({self.generate_url}). Ensure service is running: {e}")

class DecisionPipeline:
    """Decision support pipeline implementing Chain-of-Drafts (CoD) explainability."""
    def __init__(self, retriever: Optional[HybridRetriever] = None, model_name: str = "llama3.1:8b-instruct-q8_0"):
        self.retriever = retriever or HybridRetriever()
        self.llm = LocalOllamaClient(model_name=model_name)
        
        self.system_prompt = (
            "You are an expert power system security decision support AI for the Cyprus Transmission Grid.\n"
            "You MUST strictly adhere to the Chain-of-Drafts (CoD) explainability protocol.\n"
            "CRITICAL DIRECTIVE ON NUMERICAL ACCURACY:\n"
            "- You must NEVER hallucinate, estimate, or invent numerical thresholds, frequencies, time windows, or percentages.\n"
            "- Extract values verbatim from the retrieved text. If an exact number is not found in the text, explicitly state it is missing.\n\n"
            "Every response MUST be a single valid JSON object following this exact schema:\n"
            "{\n"
            '  "evidence": [{"source_doc": "<doc_name>", "section": "<clause>", "page": <page_int>, "excerpt": "<verbatim text>"}],\n'
            '  "assessment": "<In-depth engineering evaluation of system security, physical grid constraints, and exact limits. NEVER use placeholder text>",\n'
            '  "recommendation": "<Direct, actionable operational advice with precise verbatim thresholds and exceptions>",\n'
            '  "confidence": <float between 0.0 and 1.0>,\n'
            '  "confidence_rationale": "<Reasoning for the confidence score based on verbatim data sufficiency>"\n'
            "}\n"
            "Rules:\n"
            "1. Output ONLY the JSON block. Do not include markdown fences or any commentary outside the JSON.\n"
            "2. In 'evidence', quote the verbatim sentence containing the exact regulatory requirement.\n"
            "3. Base all answers strictly on the provided Cyprus Grid Code chunks."
        )

    def format_context(self, retrieved_nodes: List[Dict[str, Any]]) -> str:
        parts = []
        for idx, node in enumerate(retrieved_nodes, start=1):
            meta = node.get("metadata", {})
            src = meta.get("source", "Cyprus Regulations")
            page = meta.get("page", 0)
            sec = meta.get("section", "General")
            text = node.get("content", "").strip()
            parts.append(f"[Snippet {idx}] Source: {src} | Clause: {sec} | Page: {page}\nContent: {text}")
        return "\n\n".join(parts)

    def execute(self, query: str, top_k: int = 4, trigger_simulation: bool = False) -> Dict[str, Any]:
        retrieved_nodes = self.retriever.retrieve(query, top_k=top_k)
        context_str = self.format_context(retrieved_nodes)

        sim_result = None
        if trigger_simulation or any(w in query.lower() for w in ["simulate", "fault", "contingency", "trip", "cct"]):
            sim_result = run_contingency_simulation(query)

        prompt = f"""
Official Regulatory Ground-Truth Chunks:
{context_str}

{"External Dynamic Simulation Results:" + json.dumps(sim_result) if sim_result else ""}

Operator Operational Query:
{query}

Critical Instructions:
1. Ground Truth First: Extract EXACT numerical values and time windows verbatim from the retrieved text (e.g. check for 1.0 Hz/s over 500 ms window under clause T1.7.3.1.1). NEVER hallucinate or alter numerical thresholds like RoCoF.
2. In 'evidence': Quote the exact sentence containing the numerical value and clause.
3. In 'assessment': Explain the physical implications (e.g. system inertia constraints in an isolated island grid, rate of frequency decay, tripping risks).
4. In 'recommendation': Provide explicit limits and conditions.
5. In 'confidence': If the retrieved snippets do not contain the exact numeric threshold, set confidence < 0.6 and state missing data.

Output the strict JSON:
"""
        raw_output = self.llm.generate(prompt=prompt, system_prompt=self.system_prompt, format_json=True)

        try:
            parsed_dict = json.loads(raw_output)
            cod_output = DecisionAnalysisOutput(**parsed_dict)
            cod_output.audit_trace_id = f"AUDIT-{uuid.uuid4().hex[:8].upper()}"
        except Exception as e:
            logger.warning(f"CoD schema fallback triggered: {e}")
            cod_output = DecisionAnalysisOutput(
                evidence=[CodeEvidenceItem(source_doc="KM Version 1.1.0", section="General", excerpt="Refer to retrieved context.")],
                assessment=raw_output,
                recommendation="Consult senior shift supervisor.",
                confidence=0.5,
                confidence_rationale="Fallback triggered due to raw formatting discrepancy.",
                audit_trace_id=f"AUDIT-{uuid.uuid4().hex[:8].upper()}"
            )

        return {
            "query": query,
            "cod_trace": cod_output.model_dump(),
            "retrieved_nodes": retrieved_nodes,
            "simulation_result": sim_result,
            "model": self.llm.model_name
        }