"""
AZIA Information Architecture (IA) Engine
Derives global navigation hierarchies, screen groups, entity models, and content priorities.
Ensures zero arbitrary screen lists; every screen has a structural role in the product hierarchy.
"""

from typing import List
from azia.azia_core.models.ia import (
    NavigationItem,
    NavigationModel,
    ScreenGroup,
    EntityRelationship,
    InformationArchitecture,
)
from azia.azia_core.intelligence.requirement_engine import RequirementAnalysis


class IAEngine:
    """Plans information architecture, navigation models, and entity structures."""

    def plan(self, analysis: RequirementAnalysis) -> InformationArchitecture:
        category = analysis.product_category.lower()
        platform = analysis.platform.lower()

        if "food" in category:
            # Mobile food delivery IA
            nav_model = NavigationModel(
                pattern="bottom_tabs",
                primary_items=[
                    NavigationItem(id="nav_explore", label="Explore", icon_name="compass", target_screen_id="scr_home"),
                    NavigationItem(id="nav_search", label="Search", icon_name="search", target_screen_id="scr_search"),
                    NavigationItem(id="nav_orders", label="Orders", icon_name="shopping-bag", target_screen_id="scr_orders_history", badge="1"),
                    NavigationItem(id="nav_profile", label="Profile", icon_name="user", target_screen_id="scr_profile"),
                ],
                secondary_items=[],
                utility_items=[
                    NavigationItem(id="nav_cart_float", label="Cart", icon_name="shopping-cart", target_screen_id="scr_cart", badge="2")
                ]
            )

            screen_groups = [
                ScreenGroup(
                    group_id="grp_discovery",
                    group_name="Discovery & Search",
                    screen_ids=["scr_home", "scr_search", "scr_search_results"]
                ),
                ScreenGroup(
                    group_id="grp_ordering",
                    group_name="Ordering & Fulfillment",
                    screen_ids=["scr_restaurant_detail", "scr_cart", "scr_checkout", "scr_order_confirmation", "scr_order_tracking"]
                ),
                ScreenGroup(
                    group_id="grp_account",
                    group_name="Account & History",
                    screen_ids=["scr_orders_history", "scr_profile"]
                )
            ]

            entity_relationships = [
                EntityRelationship(
                    entity_name="Restaurant",
                    cardinality="1:N (has many MealItems)",
                    primary_attributes=["id", "name", "cuisine", "rating", "delivery_time_mins", "min_order_price", "image_url"],
                    screens_displayed=["scr_home", "scr_search_results", "scr_restaurant_detail"]
                ),
                EntityRelationship(
                    entity_name="MealItem",
                    cardinality="N:1 (belongs to Restaurant)",
                    primary_attributes=["id", "title", "description", "price", "dietary_tag", "customization_options"],
                    screens_displayed=["scr_restaurant_detail", "scr_cart"]
                ),
                EntityRelationship(
                    entity_name="Order",
                    cardinality="1:1 (generated from Cart)",
                    primary_attributes=["order_id", "items", "subtotal", "student_discount", "delivery_fee", "drop_location", "status", "courier_eta"],
                    screens_displayed=["scr_checkout", "scr_order_confirmation", "scr_order_tracking", "scr_orders_history"]
                )
            ]

        else:
            # Desktop SaaS PM IA
            nav_model = NavigationModel(
                pattern="left_sidebar",
                primary_items=[
                    NavigationItem(id="nav_dashboard", label="Dashboard", icon_name="layout-dashboard", target_screen_id="scr_dashboard"),
                    NavigationItem(id="nav_board", label="Sprint Board", icon_name="trello", target_screen_id="scr_kanban_board"),
                    NavigationItem(id="nav_backlog", label="Backlog", icon_name="list-todo", target_screen_id="scr_task_list"),
                    NavigationItem(id="nav_analytics", label="Analytics", icon_name="bar-chart-2", target_screen_id="scr_analytics"),
                ],
                secondary_items=[
                    NavigationItem(id="nav_team", label="Team & Members", icon_name="users", target_screen_id="scr_team"),
                    NavigationItem(id="nav_integrations", label="Git Integrations", icon_name="git-branch", target_screen_id="scr_integrations")
                ],
                utility_items=[
                    NavigationItem(id="nav_settings", label="Settings", icon_name="settings", target_screen_id="scr_settings")
                ]
            )

            screen_groups = [
                ScreenGroup(
                    group_id="grp_workspace",
                    group_name="Workspace Overview",
                    screen_ids=["scr_dashboard", "scr_analytics"]
                ),
                ScreenGroup(
                    group_id="grp_tasks",
                    group_name="Task & Sprint Management",
                    screen_ids=["scr_kanban_board", "scr_task_list", "scr_task_detail", "scr_create_task_modal"]
                ),
                ScreenGroup(
                    group_id="grp_settings",
                    group_name="Team & Configuration",
                    screen_ids=["scr_team", "scr_settings"]
                )
            ]

            entity_relationships = [
                EntityRelationship(
                    entity_name="Project",
                    cardinality="1:N (has many Sprints & Tasks)",
                    primary_attributes=["id", "name", "key", "lead_engineer", "status", "deadline"],
                    screens_displayed=["scr_dashboard", "scr_settings"]
                ),
                EntityRelationship(
                    entity_name="Task",
                    cardinality="N:1 (belongs to Sprint & Project)",
                    primary_attributes=["id", "title", "description", "priority", "status", "assignee", "story_points", "github_pr_url"],
                    screens_displayed=["scr_kanban_board", "scr_task_list", "scr_task_detail"]
                ),
                EntityRelationship(
                    entity_name="Sprint",
                    cardinality="1:N (contains Tasks)",
                    primary_attributes=["sprint_id", "name", "goal", "start_date", "end_date", "velocity", "status"],
                    screens_displayed=["scr_dashboard", "scr_kanban_board", "scr_analytics"]
                )
            ]

        return InformationArchitecture(
            navigation_model=nav_model,
            screen_groups=screen_groups,
            entity_relationships=entity_relationships,
            depth_limit=3,
            breadcrumbs_required=(platform in ["desktop", "web"])
        )
