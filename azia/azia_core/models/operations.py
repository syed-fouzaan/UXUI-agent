"""
AZIA Semantic Figma Operations Protocol
Strict schema for deterministic canvas operations.
Every operation guarantees non-destructive execution, layer naming, Auto Layout,
token application, and ownership tagging (managed_by='autonomous-design-mcp').
"""

from enum import Enum
from typing import List, Optional, Dict, Any, Union
from pydantic import BaseModel, Field


class FigmaOperationType(str, Enum):
    CREATE_PAGE = "create_page"
    CREATE_SECTION = "create_section"
    CREATE_SCREEN = "create_screen"
    CREATE_FRAME = "create_frame"
    CREATE_AUTO_LAYOUT = "create_auto_layout"
    CREATE_TEXT = "create_text"
    CREATE_COMPONENT = "create_component"
    CREATE_COMPONENT_VARIANT = "create_component_variant"
    CREATE_INSTANCE = "create_instance"
    CREATE_BUTTON = "create_button"
    CREATE_INPUT = "create_input"
    CREATE_CARD = "create_card"
    CREATE_LIST = "create_list"
    CREATE_GRID = "create_grid"
    CREATE_NAVIGATION = "create_navigation"
    CREATE_MODAL = "create_modal"
    CREATE_FORM = "create_form"
    CREATE_TABLE = "create_table"
    CREATE_BADGE = "create_badge"
    CREATE_STICKY_NOTE = "create_sticky_note"
    CREATE_CONNECTOR = "create_connector"
    CREATE_STATE = "create_state"
    CONNECT_PROTOTYPE = "connect_prototype"
    APPLY_DESIGN_TOKENS = "apply_design_tokens"
    UPDATE_NODE = "update_node"
    DELETE_GENERATED_CONTENT = "delete_generated_content"


class BaseFigmaOperation(BaseModel):
    """Common baseline attributes for all Figma operations."""
    op_id: str = Field(description="Unique operation sequence ID e.g. op_001")
    op_type: FigmaOperationType = Field(description="Operation type identifier")
    target_id: str = Field(description="Node ID being targeted or created")
    parent_id: Optional[str] = Field(default=None, description="Parent container node ID")
    name: str = Field(description="Figma layer name")
    managed_by: str = Field(default="autonomous-design-mcp")
    generation_id: Optional[str] = Field(default=None)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CreateScreenOp(BaseFigmaOperation):
    op_type: FigmaOperationType = FigmaOperationType.CREATE_SCREEN
    x: int = 0
    y: int = 0
    width: int = 393
    height: int = 852
    direction: str = "vertical"
    padding_top: int = 44
    padding_bottom: int = 34
    padding_x: int = 16
    gap: int = 16
    bg_color_hex: str = "#FFFFFF"
    screen_id: str = ""


class CreateComponentOp(BaseFigmaOperation):
    op_type: FigmaOperationType = FigmaOperationType.CREATE_COMPONENT
    component_id: str = ""
    width: int = 120
    height: int = 44
    auto_layout: bool = True
    direction: str = "horizontal"
    padding_x: int = 16
    padding_y: int = 12
    gap: int = 8
    corner_radius: int = 8
    bg_color_hex: str = "#2563EB"
    border_color_hex: Optional[str] = None


class CreateInstanceOp(BaseFigmaOperation):
    op_type: FigmaOperationType = FigmaOperationType.CREATE_INSTANCE
    master_component_id: str = ""
    overrides: Dict[str, Any] = Field(default_factory=dict)


class CreateTextOp(BaseFigmaOperation):
    op_type: FigmaOperationType = FigmaOperationType.CREATE_TEXT
    content: str = ""
    font_size: int = 16
    font_weight: int = 400
    color_hex: str = "#1E293B"
    alignment: str = "LEFT"
    letter_spacing: float = 0.0


class CreateCardOp(BaseFigmaOperation):
    op_type: FigmaOperationType = FigmaOperationType.CREATE_CARD
    width: int = 361
    height: Optional[int] = None
    padding: int = 16
    gap: int = 12
    corner_radius: int = 12
    bg_color_hex: str = "#FFFFFF"
    border_color_hex: Optional[str] = "#E2E8F0"
    shadow_css: Optional[str] = "0 2px 8px rgba(0,0,0,0.06)"


class CreateButtonOp(BaseFigmaOperation):
    op_type: FigmaOperationType = FigmaOperationType.CREATE_BUTTON
    label: str = "Button"
    variant: str = "primary"
    icon_name: Optional[str] = None
    bg_color_hex: str = "#2563EB"
    text_color_hex: str = "#FFFFFF"
    corner_radius: int = 8
    width: Optional[int] = None


class CreateInputOp(BaseFigmaOperation):
    op_type: FigmaOperationType = FigmaOperationType.CREATE_INPUT
    label: str = "Label"
    placeholder: str = "Enter value..."
    value: Optional[str] = None
    helper_text: Optional[str] = None
    is_required: bool = False
    corner_radius: int = 8
    border_color_hex: str = "#CBD5E1"


class CreateStickyNoteOp(BaseFigmaOperation):
    op_type: FigmaOperationType = FigmaOperationType.CREATE_STICKY_NOTE
    content: str = ""
    author: str = "AZIA AI UX Copilot"
    color_category: str = "YELLOW"  # YELLOW, BLUE, GREEN, RED, PURPLE
    x: int = 0
    y: int = 0


class CreateConnectorOp(BaseFigmaOperation):
    op_type: FigmaOperationType = FigmaOperationType.CREATE_CONNECTOR
    from_node_id: str = ""
    to_node_id: str = ""
    label: Optional[str] = None
    stroke_color_hex: str = "#64748B"
    style: str = "CURVED"  # STRAIGHT, CURVED, ELBOW


class ConnectPrototypeOp(BaseFigmaOperation):
    op_type: FigmaOperationType = FigmaOperationType.CONNECT_PROTOTYPE
    source_screen_id: str = ""
    target_screen_id: str = ""
    trigger: str = "ON_CLICK"
    animation: str = "SLIDE_IN_RIGHT"
    duration_ms: int = 300


class FigmaOperation(BaseModel):
    """Polymorphic container wrapping any Figma operation."""
    op_id: str
    op_type: FigmaOperationType
    target_id: str
    parent_id: Optional[str] = None
    name: str
    payload: Dict[str, Any] = Field(default_factory=dict)
    managed_by: str = "autonomous-design-mcp"
    generation_id: Optional[str] = None
