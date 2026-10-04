"""
AZIA Synthetic Usability Simulation & Visual Saliency Models
Defines multi-agent persona simulation, visual attention saliency heatmaps,
and funnel drop-off curves with psychological friction analysis.
"""

from enum import Enum
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class CognitiveBandwidth(str, Enum):
    HIGH = "HIGH"        # Relaxed, seated at desk, full focus
    MEDIUM = "MEDIUM"    # Standard task execution, normal distractions
    LOW = "LOW"          # Rushed, walking, multi-tasking, high distraction


class SyntheticUserAgent(BaseModel):
    """An autonomous simulated user persona."""
    id: str = Field(description="Agent ID e.g. AGENT-RUSHED-01")
    archetype: str = Field(description="Rushed Student, Tech Lead, First-time Buyer")
    cognitive_bandwidth: CognitiveBandwidth = Field(default=CognitiveBandwidth.MEDIUM)
    attention_budget_seconds: int = Field(default=45, description="Max patience before abandonment")
    price_sensitivity_1_to_10: int = Field(default=8)
    tech_literacy_1_to_10: int = Field(default=7)


class VisualFixationPoint(BaseModel):
    """Predicted visual attention fixation coordinate and saliency weight."""
    element_id: str
    element_name: str
    x_percent: float = Field(ge=0.0, le=100.0)
    y_percent: float = Field(ge=0.0, le=100.0)
    saliency_score: float = Field(ge=0.0, le=1.0, description="Visual pop-out weight")
    scanpath_order: int = Field(description="1 = first fixation, 2 = second fixation")
    noticeability_percentage: int = Field(ge=0, le=100)


class ScreenAttentionHeatmap(BaseModel):
    """Per-screen visual saliency map."""
    screen_id: str
    screen_name: str
    primary_focal_element: str
    fixations: List[VisualFixationPoint] = Field(default_factory=list)
    visual_balance_score: int = Field(ge=0, le=100, description="100 = perfectly guided attention")
    distraction_risk: str = Field(default="Low", description="Low, Medium, High")


class FunnelStepMetric(BaseModel):
    """Drop-off and retention metrics at each milestone of the user journey."""
    step_number: int
    screen_id: str
    screen_name: str
    retained_percentage: float = Field(ge=0.0, le=100.0)
    drop_off_percentage: float = Field(ge=0.0, le=100.0)
    avg_dwell_time_seconds: float
    primary_friction_cause: Optional[str] = None
    psychological_state: str = Field(description="Curious, Confident, Hesitant, Frustrated, Relieved")


class UsabilitySimulationReport(BaseModel):
    """Consolidated Synthetic Usability & Attention Report."""
    simulation_run_id: str
    total_simulated_sessions: int = Field(default=1000)
    overall_funnel_conversion_rate: float = Field(description="Percentage completing end-to-end task")
    avg_time_to_completion_seconds: float
    highest_dropoff_screen_id: str
    highest_dropoff_reason: str
    funnel_steps: List[FunnelStepMetric] = Field(default_factory=list)
    screen_heatmaps: List[ScreenAttentionHeatmap] = Field(default_factory=list)
    mitigation_recommendations: List[str] = Field(default_factory=list)
