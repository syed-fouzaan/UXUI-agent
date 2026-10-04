"""
AZIA QA & Validation Models
Dual-track QA: Visual layout & design system adherence + UX Requirement coverage verification.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from azia.azia_core.models.taxonomy import Severity


class QACheckResult(BaseModel):
    """Result of a single deterministic QA check."""
    check_id: str = Field(description="Unique check identifier e.g. QA-VIS-01")
    name: str = Field(description="e.g. 8pt Grid Alignment Check")
    passed: bool = Field(default=True)
    score: float = Field(default=1.0, ge=0.0, le=1.0)
    details: str = Field(description="Findings or diagnostic details")
    severity: Severity = Field(default=Severity.LOW)
    recommended_fix: Optional[str] = Field(default=None)


class RequirementCoverageItem(BaseModel):
    """Verification that a specific requirement is satisfied by screens & components."""
    requirement_statement: str = Field(description="Original user need/feature")
    status: str = Field(default="FULLY_COVERED", description="FULLY_COVERED, PARTIAL, MISSING")
    covered_by_screens: List[str] = Field(default_factory=list)
    covered_by_components: List[str] = Field(default_factory=list)
    validation_notes: str = Field(description="How this is verified in the UX flow")


RequirementCoverage = RequirementCoverageItem


class VisualQAReport(BaseModel):
    """Automated visual layout and design system adherence report."""
    grid_alignment_passed: bool = Field(default=True)
    typography_scale_passed: bool = Field(default=True)
    contrast_accessibility_passed: bool = Field(default=True)
    component_reuse_ratio: float = Field(default=0.92, description="Percentage of elements using master components")
    visual_density_rating: str = Field(default="Balanced", description="Too Sparse, Balanced, Too Dense")
    checks: List[QACheckResult] = Field(default_factory=list)


class ComprehensiveQAReport(BaseModel):
    """Master QA and Verification Report."""
    overall_qa_score_100: int = Field(default=95)
    requirement_coverage_percentage: float = Field(default=100.0)
    visual_qa: VisualQAReport
    requirements_breakdown: List[RequirementCoverageItem] = Field(default_factory=list)
    repair_iterations_applied: int = Field(default=0)
    issues_resolved: List[str] = Field(default_factory=list)
    unresolved_issues: List[str] = Field(default_factory=list)
    is_ready_for_production: bool = Field(default=True)
