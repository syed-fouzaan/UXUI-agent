"""
AZIA Screen Planning Models
Full screen specifications including Auto Layout parameters, responsive constraints,
semantic sections, content hierarchy, component instances, and state variations.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class ScreenLayout(BaseModel):
    """Layout engine parameters for a screen."""
    width: int = Field(default=393, description="Frame width (e.g. 393 for mobile, 1280 for web)")
    height: int = Field(default=852, description="Frame height (e.g. 852 for mobile, 900 for web)")
    direction: str = Field(default="vertical", description="vertical, horizontal")
    padding_top: int = Field(default=44, description="Top padding / safe area")
    padding_bottom: int = Field(default=34, description="Bottom padding / home indicator")
    padding_left: int = Field(default=16)
    padding_right: int = Field(default=16)
    gap: int = Field(default=16)
    background_token_ref: str = Field(default="background")
    scrollable: bool = Field(default=True)


class ComponentInstanceSpec(BaseModel):
    """An instance of a reusable component placed inside a screen section."""
    instance_id: str = Field(description="Unique instance ID on this screen")
    component_ref: str = Field(description="Master component ID e.g. cmp_card_restaurant")
    name: str = Field(description="Semantic layer name in Figma")
    layout_mode: str = Field(default="fill", description="fill, hug, fixed")
    content_data: Dict[str, Any] = Field(default_factory=dict, description="Real domain content props")
    variant_ref: Optional[str] = Field(default=None)
    interactive_target_screen_id: Optional[str] = Field(default=None)


ScreenComponentInstance = ComponentInstanceSpec


class ScreenSection(BaseModel):
    """A logical visual container/group inside a screen."""
    section_id: str = Field(description="Unique section ID e.g. sec_header, sec_popular_list")
    title: str = Field(description="Section heading or semantic identifier")
    direction: str = Field(default="vertical", description="vertical, horizontal, grid")
    gap: int = Field(default=12)
    padding: int = Field(default=0)
    layout_mode: str = Field(default="fill", description="fill, hug, fixed")
    components: List[ComponentInstanceSpec] = Field(default_factory=list)


class ScreenStateVariation(BaseModel):
    """Alternative states for a screen (empty, error, loading, filtered)."""
    state_type: str = Field(description="empty, loading, error, success, filter_active")
    trigger_condition: str = Field(description="When this state is triggered")
    visual_changes_description: str = Field(description="What changes on screen")
    active_component_replacements: Dict[str, str] = Field(default_factory=dict)


ScreenState = ScreenStateVariation


class ScreenSpec(BaseModel):
    """Complete specification of a single product screen."""
    screen_id: str = Field(description="Unique screen identifier e.g. scr_home, scr_restaurant_detail")
    screen_name: str = Field(description="Descriptive screen name e.g. Restaurant Discovery Feed")
    purpose: str = Field(description="Primary UX reason for this screen to exist")
    user_goal: str = Field(description="What the user intends to achieve here")
    entry_conditions: List[str] = Field(default_factory=list, description="Preconditions to reach this screen")
    exit_actions: List[str] = Field(default_factory=list, description="Actions navigating away")
    primary_cta: str = Field(description="Main call-to-action button or affordance")
    secondary_actions: List[str] = Field(default_factory=list)
    content_hierarchy: List[str] = Field(description="Ordered list of visual importance")
    layout: ScreenLayout = Field(default_factory=ScreenLayout)
    sections: List[ScreenSection] = Field(default_factory=list)
    states: List[ScreenStateVariation] = Field(default_factory=list)
    navigation_bar_visible: bool = Field(default=True)
    prototype_destinations: Dict[str, str] = Field(
        default_factory=dict,
        description="Map of element/instance_id -> target_screen_id"
    )
