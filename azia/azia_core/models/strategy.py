"""
AZIA Non-Disruptive Launch Strategy Models
Analyzes delta between existing user behaviors and new functionality.
Formulates Progressive Disclosure, Opt-In Toggles, Contextual Onboarding, and Safe Fallback workflows.
"""

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class RolloutMechanism(str, Enum):
    PROGRESSIVE_DISCLOSURE = "PROGRESSIVE_DISCLOSURE"
    OPT_IN_TOGGLE = "OPT_IN_TOGGLE"
    CONTEXTUAL_ONBOARDING = "CONTEXTUAL_ONBOARDING"
    PARALLEL_RUN = "PARALLEL_RUN"
    PHASED_COHORT = "PHASED_COHORT"


class FallbackWorkflow(BaseModel):
    """Guaranteed safety net when new feature encounters failure or rejection."""
    failure_trigger: str = Field(description="Network error, missing data, user cancels, lack of permission")
    fallback_behavior: str = Field(description="How system responds cleanly without locking the user out")
    preserves_data: bool = Field(default=True, description="Whether user draft/state is preserved")
    user_messaging: str = Field(description="Honest, clear, non-jargon message shown to user")


class NonDisruptiveStrategy(BaseModel):
    """Holistic strategy to prevent user disruption during new feature introduction."""
    existing_flow_risk: RiskLevel = Field(default=RiskLevel.MEDIUM)
    primary_risks: List[str] = Field(default_factory=list, description="Identified cognitive or workflow risks")
    recommended_mechanism: RolloutMechanism = Field(default=RolloutMechanism.PROGRESSIVE_DISCLOSURE)
    progressive_disclosure_steps: List[str] = Field(
        default_factory=list,
        description="Step 1: Baseline entry, Step 2: In-context teaser, Step 3: Full controls"
    )
    opt_in_toggle_spec: Optional[str] = Field(default=None, description="Where and how user can toggle off new experience")
    contextual_onboarding_trigger: str = Field(description="Exact user moment when educational tooltip/coach mark appears")
    safe_fallbacks: List[FallbackWorkflow] = Field(default_factory=list)
    impact_score_1_to_10: int = Field(default=4, description="Disruption impact score (lower is safer)")
