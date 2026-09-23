import json
import logging
from pathlib import Path
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from src.orchestration.pipeline import DecisionPipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Cyprus Grid Safety Decision Support System",
    description="Local HPC High-Security DSA Engine implementing Chain-of-Drafts (CoD) Explainability Protocol"
)

pipeline: Optional[DecisionPipeline] = None

class QueryRequest(BaseModel):
    query: str
    top_k: int = 4
    trigger_simulation: bool = False

class OverrideRequest(BaseModel):
    audit_trace_id: str
    operator_id: str
    action: str = Field(..., description="ACCEPT, CHALLENGE, or OVERRIDE")
    override_reason: str
    modified_recommendation: Optional[str] = None

@app.on_event("startup")
def startup_event():
    global pipeline
    logger.info("Initializing local DecisionPipeline and vector retrieval index...")
    pipeline = DecisionPipeline()
    logger.info("Decision engine ready. Connected to local LLaMA-3.1-8B-Instruct (8-bit).")

@app.get("/health")
def health_check():
    """Health endpoint polled by scripts/run_system.sh"""
    if pipeline is not None:
        return {"status": "HEALTHY", "model": pipeline.llm.model_name}
    return {"status": "INITIALIZING"}

@app.post("/api/decision")
def get_decision(req: QueryRequest):
    if not pipeline:
        raise HTTPException(status_code=503, detail="Pipeline service not initialized")
    try:
        result = pipeline.execute(
            query=req.query,
            top_k=req.top_k,
            trigger_simulation=req.trigger_simulation
        )
        return result
    except Exception as e:
        logger.error(f"Decision execution error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/audit/override")
def record_override(req: OverrideRequest):
    audit_record = {
        "timestamp": datetime.utcnow().isoformat(),
        "audit_trace_id": req.audit_trace_id,
        "operator_id": req.operator_id,
        "action": req.action,
        "reason": req.override_reason,
        "modified_recommendation": req.modified_recommendation
    }
    audit_log_path = Path("data/simulation/audit_logs.jsonl")
    audit_log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(audit_log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(audit_record, ensure_ascii=False) + "\n")
    return {"status": "SUCCESS", "message": f"Audit trace {req.audit_trace_id} logged successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.server.app:app", host="0.0.0.0", port=8000, reload=False)