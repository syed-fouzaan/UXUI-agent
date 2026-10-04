"""
AZIA Component Architecture Models
Semantic component definitions, variant matrices, and Auto Layout structures.
Guarantees component reusability across screens instead of ad-hoc manual shapes.
"""

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class ComponentType(str, Enum):
    BUTTON = "BUTTON"
    ICON_BUTTON = "ICON_BUTTON"
    INPUT = "INPUT"
    SEARCH_BAR = "SEARCH_BAR"
    SELECT = "SELECT"
    CHECKBOX = "CHECKBOX"
    RADIO = "RADIO"
    TOGGLE = "TOGGLE"
    CARD = "CARD"
    LIST = "LIST"
    GRID = "GRID"
    NAVBAR = "NAVBAR"
    SIDEBAR = "SIDEBAR"
    TABS = "TABS"
    BREADCRUMBS = "BREADCRUMBS"
    BADGE = "BADGE"
    AVATAR = "AVATAR"
    MODAL = "MODAL"
    DIALOG = "DIALOG"
    BOTTOM_SHEET = "BOTTOM_SHEET"
    FORM = "FORM"
    TABLE = "TABLE"
    BANNER = "BANNER"
    ALERT = "ALERT"
    TOOLTIP = "TOOLTIP"
    PAGINATION = "PAGINATION"
    PROGRESS = "PROGRESS"
    CHART = "CHART"
    LOADING = "LOADING"
    EMPTY_STATE = "EMPTY_STATE"
    ERROR_STATE = "ERROR_STATE"
    SUCCESS_STATE = "SUCCESS_STATE"


class ComponentVariant(BaseModel):
    """Specific variant state of a reusable component."""
    variant_id: str = Field(description="e.g. primary_default, primary_hover, secondary_disabled")
    name: str = Field(description="Human readable variant name")
    state: str = Field(default="default", description="default, hover, active, focused, disabled, loading")
    size: str = Field(default="medium", description="small, medium, large")
    properties: Dict[str, Any] = Field(default_factory=dict, description="Visual style overrides: bg, color, border")


class ComponentDefinition(BaseModel):
    """Reusable semantic component schema."""
    component_id: str = Field(description="Unique component master ID e.g. cmp_button_primary")
    name: str = Field(description="Component name e.g. Primary Action Button")
    type: ComponentType = Field(description="Underlying semantic type")
    description: str = Field(description="Usage guideline and accessibility notes")
    default_width: int = Field(default=120)
    default_height: int = Field(default=44)
    auto_layout_direction: str = Field(default="horizontal", description="horizontal, vertical, none")
    padding_x: int = Field(default=16)
    padding_y: int = Field(default=12)
    gap: int = Field(default=8)
    corner_radius: int = Field(default=8)
    bg_token_ref: str = Field(default="primary")
    text_token_ref: str = Field(default="text_primary")
    border_token_ref: Optional[str] = Field(default=None)
    variants: List[ComponentVariant] = Field(default_factory=list)
    nested_component_ids: List[str] = Field(default_factory=list)


class ComponentRegistry(BaseModel):
    """Central component library supporting instance reuse."""
    components: Dict[str, ComponentDefinition] = Field(default_factory=dict)

    def register(self, component: ComponentDefinition) -> None:
        self.components[component.component_id] = component

    def get(self, component_id: str) -> Optional[ComponentDefinition]:
        return self.components.get(component_id)
