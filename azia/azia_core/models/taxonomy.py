"""
AZIA Cognitive & Epistemic Taxonomy Models
Tracks knowledge status, evidence grounding, confidence levels, and assumptions.
Ensures zero hallucinations are presented as facts.
"""

from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class EpistemicStatus(str, Enum):
    CONFIRMED = "CONFIRMED"      # Directly explicitly stated in user input/documents
    INFERRED = "INFERRED"        # Reasonably derived based on UX patterns and domain facts
    ASSUMPTION = "ASSUMPTION"    # Design hypothesis that requires validation
    UNKNOWN = "UNKNOWN"          # Unspecified critical gap requiring clarification


class ConfidenceLevel(str, Enum):
    HIGH = "HIGH"        # 85-100% confidence, backed by multiple evidence points
    MEDIUM = "MEDIUM"    # 60-84% confidence, standard industry heuristic
    LOW = "LOW"          # <60% confidence, speculative hypothesis


class Severity(str, Enum):
    CRITICAL = "CRITICAL"  # Blocker: breaks usability, core task failure, severe accessibility violation
    HIGH = "HIGH"          # High friction, significant user error likelihood
    MEDIUM = "MEDIUM"      # Moderate inconvenience, inconsistency, minor cognitive load
    LOW = "LOW"            # Cosmetic or subtle micro-optimization


class EvidenceItem(BaseModel):
    """Traceable ground-truth evidence anchor."""
    id: str = Field(description="Unique identifier e.g. EVID-001")
    source: str = Field(description="Origin source document or quote, e.g. PRD Section 4 or User Prompt")
    snippet: str = Field(description="The extracted excerpt or observation")
    category: str = Field(default="user_requirement", description="user_need, constraint, business_goal, tech_limit")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.HIGH)


class AssumptionItem(BaseModel):
    """An explicit design hypothesis requiring ongoing validation."""
    id: str = Field(description="Unique identifier e.g. ASM-001")
    statement: str = Field(description="What is assumed")
    basis: str = Field(description="Why this assumption was made (heuristic, industry standard)")
    affected_components: List[str] = Field(default_factory=list)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.MEDIUM)
    validation_status: str = Field(default="PENDING_TESTING")
    recommended_validation_method: str = Field(
        default="Usability testing with 5 participants",
        description="A/B test, 5-second test, analytics event, interview"
    )


class EpistemicRegister(BaseModel):
    """Comprehensive knowledge register distinguishing verified facts from hypotheses."""
    confirmed_facts: List[EvidenceItem] = Field(default_factory=list)
    inferred_insights: List[Dict[str, Any]] = Field(default_factory=list)
    explicit_assumptions: List[AssumptionItem] = Field(default_factory=list)
    critical_unknowns: List[str] = Field(default_factory=list)
