"""
AZIA UX Audit & Heuristic Evaluation Models
Based on Jakob Nielsen's 10 Usability Heuristics, WCAG 2.1 AA accessibility standards,
and Cognitive Load theory. Produces actionable, evidence-linked design findings.
"""

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from azia.azia_core.models.taxonomy import Severity, ConfidenceLevel


class HeuristicType(str, Enum):
    VISIBILITY_OF_STATUS = "Visibility of System Status"
    MATCH_SYSTEM_AND_REAL_WORLD = "Match Between System and the Real World"
    USER_CONTROL_AND_FREEDOM = "User Control and Freedom"
    CONSISTENCY_AND_STANDARDS = "Consistency and Standards"
    ERROR_PREVENTION = "Error Prevention"
    RECOGNITION_OVER_RECALL = "Recognition Rather Than Recall"
    FLEXIBILITY_AND_EFFICIENCY = "Flexibility and Efficiency of Use"
    AESTHETIC_AND_MINIMALIST = "Aesthetic and Minimalist Design"
    RECOGNIZE_AND_RECOVER = "Help Users Recognize, Diagnose, and Recover from Errors"
    HELP_AND_DOCUMENTATION = "Help and Documentation"


class AuditFinding(BaseModel):
    """An individual actionable UX audit finding."""
    id: str = Field(description="Finding identifier e.g. FND-01")
    title: str = Field(description="Concise issue title e.g. Destructive delete missing double confirmation")
    category: str = Field(default="Usability", description="Usability, Accessibility, Cognitive Load, Error Prevention")
    severity: Severity = Field(default=Severity.MEDIUM)
    heuristic: HeuristicType = Field(default=HeuristicType.ERROR_PREVENTION)
    screen_id: Optional[str] = Field(default=None)
    affected_element: str = Field(description="The component or workflow involved")
    problem: str = Field(description="Exact issue observed")
    why_it_matters: str = Field(description="Direct impact on user task completion or cognitive fatigue")
    evidence: str = Field(description="Observation source")
    ux_principle: str = Field(description="Authoritative UX principle or law violated (e.g. Hick's Law, Fitts's Law)")
    confidence_percentage: int = Field(default=85, ge=0, le=100)
    recommendation: str = Field(description="Clear, actionable prescription for fixing the issue")
    impact: str = Field(default="High", description="High, Medium, Low")
    effort: str = Field(default="Low", description="High, Medium, Low")
    risk: str = Field(default="Low", description="Risk of making this change")
    validation_test: str = Field(default="5-user usability benchmark test")


class UXAuditReport(BaseModel):
    """Consolidated UX Audit Report."""
    overall_usability_score_100: int = Field(default=88)
    cognitive_load_level: str = Field(default="Optimal", description="Low, Optimal, High, Overwhelming")
    accessibility_rating: str = Field(default="WCAG 2.1 AA Compliant")
    critical_count: int = Field(default=0)
    high_count: int = Field(default=0)
    medium_count: int = Field(default=0)
    low_count: int = Field(default=0)
    findings: List[AuditFinding] = Field(default_factory=list)
    mentor_summary: str = Field(description="Warm, balanced critic critique from AZIA")
