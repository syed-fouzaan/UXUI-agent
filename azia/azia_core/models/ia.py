"""
AZIA Information Architecture (IA) Models
Defines navigation structures, taxonomy, screen grouping, and content hierarchy.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class NavigationItem(BaseModel):
    """An individual item in the global or contextual navigation."""
    id: str = Field(description="Unique nav item identifier")
    label: str = Field(description="Display label e.g. Explore, Orders, Profile")
    icon_name: str = Field(description="Semantic icon name e.g. compass, shopping-bag, user")
    target_screen_id: str = Field(description="ID of the screen this links to")
    badge: Optional[str] = Field(default=None, description="Optional badge e.g. '3', 'New'")
    is_primary: bool = Field(default=True)


class NavigationModel(BaseModel):
    """System-level navigation paradigm."""
    pattern: str = Field(
        default="bottom_tabs",
        description="bottom_tabs, left_sidebar, top_navbar, app_bar_with_drawer, split_view"
    )
    primary_items: List[NavigationItem] = Field(default_factory=list)
    secondary_items: List[NavigationItem] = Field(default_factory=list)
    utility_items: List[NavigationItem] = Field(default_factory=list, description="Settings, Logout, Search trigger")


class ScreenGroup(BaseModel):
    """Logical clustering of related screens."""
    group_id: str = Field(description="Unique group identifier e.g. grp_checkout")
    group_name: str = Field(description="Descriptive name e.g. Checkout & Fulfillment Flow")
    screen_ids: List[str] = Field(default_factory=list)
    parent_group_id: Optional[str] = Field(default=None)


class EntityRelationship(BaseModel):
    """Data entity representation and how it appears across the interface."""
    entity_name: str = Field(description="e.g. Restaurant, Meal, Order, Project, Task")
    cardinality: str = Field(description="e.g. 1:N, N:M")
    primary_attributes: List[str] = Field(default_factory=list)
    screens_displayed: List[str] = Field(default_factory=list)


class InformationArchitecture(BaseModel):
    """Complete IA specification."""
    navigation_model: NavigationModel
    screen_groups: List[ScreenGroup] = Field(default_factory=list)
    entity_relationships: List[EntityRelationship] = Field(default_factory=list)
    depth_limit: int = Field(default=3, description="Maximum click depth to reach primary value")
    breadcrumbs_required: bool = Field(default=False)
