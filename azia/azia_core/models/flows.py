"""
AZIA User Flow Models
Graph-based user journey representations with automated topological flow validation.
Detects dead-ends, missing error branches, unconfirmed states, and unreachable screens.
"""

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class FlowNodeType(str, Enum):
    ENTRY = "ENTRY"
    SCREEN = "SCREEN"
    USER_ACTION = "USER_ACTION"
    DECISION = "DECISION"
    SYSTEM_PROCESSING = "SYSTEM_PROCESSING"
    CONFIRMATION = "CONFIRMATION"
    SUCCESS = "SUCCESS"
    ERROR_RECOVERY = "ERROR_RECOVERY"


class FlowNode(BaseModel):
    """A single step or state in a user flow graph."""
    id: str = Field(description="Unique node ID e.g. node_home, node_tap_checkout")
    label: str = Field(description="Human readable title")
    type: FlowNodeType = Field(default=FlowNodeType.SCREEN)
    screen_id: Optional[str] = Field(default=None, description="Associated screen ID if mapped to a physical screen")
    user_action: Optional[str] = Field(default=None, description="What the user physically does: taps button, swipes, enters text")
    system_response: Optional[str] = Field(default=None, description="How the application responds")
    state_description: Optional[str] = Field(default=None, description="Current visual or data state")
    required_inputs: List[str] = Field(default_factory=list, description="Inputs required to proceed")
    potential_failures: List[str] = Field(default_factory=list, description="Potential errors (e.g. card declined, no network)")


class FlowEdge(BaseModel):
    """A directed transition between two nodes."""
    source_id: str = Field(description="Origin node ID")
    target_id: str = Field(description="Destination node ID")
    trigger: str = Field(default="click", description="Action trigger: click, submit, swipe, auto_timeout, error")
    condition: Optional[str] = Field(default=None, description="Guard condition e.g. 'cart is empty', 'authenticated'")


class UserFlow(BaseModel):
    """Complete user flow graph."""
    flow_id: str = Field(description="Unique flow ID e.g. flow_primary_order")
    title: str = Field(description="Flow title e.g. Discovery to Fulfillment Happy Path")
    description: str = Field(description="Purpose of this flow")
    entry_point_id: str = Field(description="ID of the starting node")
    exit_point_ids: List[str] = Field(default_factory=list, description="IDs of completion or terminal nodes")
    nodes: List[FlowNode] = Field(default_factory=list)
    edges: List[FlowEdge] = Field(default_factory=list)
    is_happy_path: bool = Field(default=True)


class FlowValidationResult(BaseModel):
    """Result of algorithmic flow health inspection."""
    is_valid: bool = Field(description="Whether the flow satisfies all structural UX criteria")
    dead_ends: List[str] = Field(default_factory=list, description="Non-terminal nodes with no outgoing edges")
    unreachable_nodes: List[str] = Field(default_factory=list, description="Nodes with no incoming edges from entry")
    missing_confirmation_states: List[str] = Field(default_factory=list, description="High-stakes actions lacking confirmation")
    missing_error_recovery_paths: List[str] = Field(default_factory=list, description="Actions with known failure modes lacking recovery")
    missing_back_navigation: List[str] = Field(default_factory=list, description="Screens lacking return paths")
    unnecessary_steps_detected: List[str] = Field(default_factory=list, description="Redundant steps causing friction")
