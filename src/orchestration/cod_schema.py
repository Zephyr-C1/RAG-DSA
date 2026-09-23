from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class CodeEvidenceItem(BaseModel):
    source_doc: str = Field(..., description="Citing document, e.g. KM Version 1.1.0 or Operating Margin Policy")
    section: str = Field(..., description="Specific regulatory article, e.g., T1.8.2.1, T5.3.4")
    page: Optional[int] = Field(None, description="Page number of the cited clause")
    excerpt: str = Field(..., description="Verbatim technical requirement extracted from knowledge base")

class DecisionAnalysisOutput(BaseModel):
    """
    Chain-of-Drafts (CoD) Explainability Protocol Output Schema.
    Reasoning sequence: evidence -> assessment -> recommendation -> confidence
    """
    evidence: List[CodeEvidenceItem] = Field(
        ..., 
        description="Factual regulatory citations and telemetry evidence used as baseline"
    )
    assessment: str = Field(
        ..., 
        description="Step-by-step engineering analysis evaluating security limits, RoCoF, or operating margins"
    )
    recommendation: str = Field(
        ..., 
        description="Concrete, actionable dispatch directives (e.g., active power curtailment, reserve call)"
    )
    confidence: float = Field(
        ..., 
        ge=0.0, 
        le=1.0, 
        description="Calibrated confidence level based on context sufficiency and simulation alignment"
    )
    confidence_rationale: str = Field(
        ..., 
        description="Justification for confidence score and assumptions made"
    )
    audit_trace_id: Optional[str] = Field(None, description="Unique audit event identifier for post-event analysis")
    operator_override: Optional[Dict[str, Any]] = Field(default=None, description="Container for operator challenge or override")