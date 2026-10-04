"""
AZIA UX Architecture Models
Evidence-grounded User Personas, Jobs-to-be-Done (JTBD), Mental Models, and Journeys.
Prevents hallucinated demographics while emphasizing user motivations and constraints.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from azia.azia_core.models.taxonomy import EpistemicStatus, ConfidenceLevel


class Persona(BaseModel):
    """Evidence-backed User Persona."""
    id: str = Field(description="Unique ID e.g. PER-01")
    name: str = Field(description="Representative persona label e.g. The Rushed Engineering Lead")
    role: str = Field(description="Professional role or archetype")
    primary_goal: str = Field(description="What they must achieve through the product")
    core_needs: List[str] = Field(description="Essential functional and psychological needs")
    pain_points: List[str] = Field(description="Current blockers, friction, or cognitive fatigue")
    context_of_use: str = Field(description="Environment: mobile on subway, desktop with multiple monitors, etc.")
    mental_model: str = Field(description="Pre-existing expectation of how tools in this category behave")
    tech_savviness: str = Field(default="Intermediate", description="Beginner, Intermediate, Advanced")
    supporting_evidence_ids: List[str] = Field(default_factory=list)
    epistemic_status: EpistemicStatus = Field(default=EpistemicStatus.INFERRED)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.HIGH)


class JTBD(BaseModel):
    """Jobs-To-Be-Done framework representation: When [situation], I want to [action], So I can [outcome]."""
    id: str = Field(description="Unique ID e.g. JTBD-01")
    persona_id: str = Field(description="Associated persona ID")
    situation: str = Field(description="When...")
    motivation: str = Field(description="I want to...")
    expected_outcome: str = Field(description="So I can...")
    success_metric: str = Field(description="How the user measures success (e.g. under 2 minutes, zero errors)")
    priority: str = Field(default="High", description="Core, Secondary, Delighter")
    supporting_evidence_ids: List[str] = Field(default_factory=list)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.HIGH)


class JourneyPhase(BaseModel):
    """A distinct milestone in the user's end-to-end journey."""
    phase_name: str = Field(description="Discovery, Onboarding, Task Execution, Confirmation, Retention")
    user_thought: str = Field(description="Internal monologue or cognitive state")
    touchpoints: List[str] = Field(description="Screens or channels involved")
    friction_risk: str = Field(description="Potential drop-off or confusion hazard")
    mitigation_strategy: str = Field(description="UX pattern preventing the failure")


class UserJourney(BaseModel):
    """Comprehensive user journey mapping out cognitive progression."""
    id: str = Field(description="Unique ID e.g. JRN-01")
    title: str = Field(description="Journey title e.g. First-Time Food Order")
    persona_id: str = Field(description="Target persona ID")
    phases: List[JourneyPhase] = Field(default_factory=list)
    entry_point: str = Field(description="How the user enters the journey")
    success_state: str = Field(description="Definition of journey completion")


class UXArchitecture(BaseModel):
    """Consolidated UX Architecture specification."""
    product_purpose: str = Field(description="Core purpose and value proposition")
    target_audiences: List[str] = Field(description="List of target user groups")
    personas: List[Persona] = Field(default_factory=list)
    jtbd_list: List[JTBD] = Field(default_factory=list)
    primary_journey: UserJourney = Field(description="The primary critical user path")
    secondary_journeys: List[UserJourney] = Field(default_factory=list)
    key_mental_models: List[str] = Field(default_factory=list)
