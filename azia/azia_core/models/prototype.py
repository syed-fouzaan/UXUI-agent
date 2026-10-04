"""
AZIA Prototyping Models
Deterministic interaction graphs and animated transitions for Figma prototypes.
"""

from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class InteractionTrigger(str, Enum):
    ON_CLICK = "ON_CLICK"
    ON_HOVER = "ON_HOVER"
    ON_DRAG = "ON_DRAG"
    AFTER_TIMEOUT = "AFTER_TIMEOUT"
    KEY_PRESS = "KEY_PRESS"


class TransitionAnimation(str, Enum):
    INSTANT = "INSTANT"
    SMART_ANIMATE = "SMART_ANIMATE"
    SLIDE_IN_RIGHT = "SLIDE_IN_RIGHT"
    SLIDE_IN_BOTTOM = "SLIDE_IN_BOTTOM"
    DISSOLVE = "DISSOLVE"


class PrototypeConnection(BaseModel):
    """A verified interaction link between a source affordance and destination screen."""
    id: str = Field(description="Unique connection ID e.g. conn_01")
    source_screen_id: str = Field(description="ID of origin screen")
    source_element_id: str = Field(description="ID of clickable instance/node")
    source_element_label: str = Field(description="Human label of trigger button/card")
    target_screen_id: str = Field(description="Destination screen ID")
    trigger: InteractionTrigger = Field(default=InteractionTrigger.ON_CLICK)
    animation: TransitionAnimation = Field(default=TransitionAnimation.SLIDE_IN_RIGHT)
    duration_ms: int = Field(default=300)
    user_intent: str = Field(description="Why the user takes this action")


class PrototypeGraph(BaseModel):
    """Complete prototype navigation graph."""
    start_screen_id: str = Field(description="Initial landing screen")
    connections: List[PrototypeConnection] = Field(default_factory=list)
