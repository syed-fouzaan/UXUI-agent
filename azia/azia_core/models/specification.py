"""
AZIA Unified Product Design Specification Model
The single authoritative structured schema representing the entire designed product.
Validated rigorously prior to rendering into Figma.
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

from azia.azia_core.models.taxonomy import EpistemicRegister
from azia.azia_core.models.preflight import PreFlightEvaluation
from azia.azia_core.models.ux_artifacts import UXArchitecture
from azia.azia_core.models.ia import InformationArchitecture
from azia.azia_core.models.flows import UserFlow
from azia.azia_core.models.design_system import DesignSystemTokens
from azia.azia_core.models.components import ComponentRegistry
from azia.azia_core.models.screens import ScreenSpec
from azia.azia_core.models.prototype import PrototypeGraph
from azia.azia_core.models.strategy import NonDisruptiveStrategy
from azia.azia_core.models.audit import UXAuditReport
from azia.azia_core.models.qa import ComprehensiveQAReport


class ProductMetadata(BaseModel):
    """Metadata regarding the generated product."""
    product_id: str = Field(description="Unique product identifier e.g. prd_food_delivery_01")
    product_name: str = Field(description="Product title e.g. CraveBite Campus")
    product_category: str = Field(description="e.g. On-Demand Food Delivery, Developer Tooling SaaS")
    requirement_prompt: str = Field(description="Raw user requirement prompt")
    platform: str = Field(default="mobile", description="mobile, web, tablet, desktop")
    style_direction: str = Field(default="modern", description="modern, minimal, enterprise, playful, premium")
    generation_id: str = Field(description="Unique generation run ID")
    managed_by: str = Field(default="autonomous-design-mcp")
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())


class ProductDesignSpecification(BaseModel):
    """Authoritative, fully-validated Product Design Specification."""
    metadata: ProductMetadata
    preflight: PreFlightEvaluation
    epistemic_register: EpistemicRegister
    ux_architecture: UXArchitecture
    information_architecture: InformationArchitecture
    user_flows: List[UserFlow] = Field(default_factory=list)
    design_system: DesignSystemTokens
    component_registry: ComponentRegistry
    screens: List[ScreenSpec] = Field(default_factory=list)
    prototype: PrototypeGraph
    non_disruptive_strategy: NonDisruptiveStrategy
    audit_report: Optional[UXAuditReport] = Field(default=None)
    qa_report: Optional[ComprehensiveQAReport] = Field(default=None)
    simulation_report: Optional[Any] = Field(default=None)
