"""
AZIA Pre-Flight Evaluation Models
Detects vague, under-specified, or ambiguous input before generation.
Generates targeted high-value clarification questions.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class ClarificationQuestion(BaseModel):
    """A targeted question posed to the designer when critical context is missing."""
    id: str = Field(description="Question ID e.g. Q-01")
    dimension: str = Field(description="Missing dimension: target_user, primary_goal, constraints, platform, business_metric")
    question: str = Field(description="The question prompt")
    rationale: str = Field(description="Why answering this is critical for the UX architecture")
    suggested_answers: List[str] = Field(default_factory=list, description="Smart default suggestions")
    is_blocking: bool = Field(default=False, description="Whether generation cannot safely proceed without this")


class PreFlightEvaluation(BaseModel):
    """Outcome of pre-flight ambiguity inspection."""
    is_sufficient: bool = Field(description="Whether input context meets threshold for autonomous generation")
    context_score: float = Field(ge=0.0, le=1.0, description="0.0 to 1.0 contextual completeness score")
    summary: str = Field(description="Summary of the evaluation")
    identified_intent: str = Field(description="Understood core intent")
    missing_critical_dimensions: List[str] = Field(default_factory=list)
    clarification_questions: List[ClarificationQuestion] = Field(default_factory=list)
    can_proceed_with_assumptions: bool = Field(
        default=True,
        description="Whether safe sensible UX assumptions can bridge the gaps if user opts to proceed"
    )
