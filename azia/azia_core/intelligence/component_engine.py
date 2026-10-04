"""
AZIA Component Architecture Engine
Constructs the central reusable ComponentRegistry for the product.
Ensures every screen instantiates standard components rather than drawing disconnected vector rectangles.
"""

from typing import Dict
from azia.azia_core.models.components import (
    ComponentType,
    ComponentVariant,
    ComponentDefinition,
    ComponentRegistry,
)
from azia.azia_core.intelligence.requirement_engine import RequirementAnalysis


class ComponentEngine:
    """Builds a comprehensive semantic component library tailored to the product form factor."""

    def build_registry(self, analysis: RequirementAnalysis) -> ComponentRegistry:
        registry = ComponentRegistry()
        platform = analysis.platform.lower()

        # 1. Primary Action Button
        registry.register(ComponentDefinition(
            component_id="cmp_btn_primary",
            name="Primary Action Button",
            type=ComponentType.BUTTON,
            description="Main conversion trigger with high visual emphasis and active click state.",
            default_width=320 if platform == "mobile" else 140,
            default_height=48 if platform == "mobile" else 36,
            auto_layout_direction="horizontal",
            padding_x=16,
            padding_y=12,
            gap=8,
            corner_radius=10 if platform == "mobile" else 6,
            bg_token_ref="primary",
            text_token_ref="text_on_primary",
            variants=[
                ComponentVariant(variant_id="primary_default", name="Default", state="default"),
                ComponentVariant(variant_id="primary_hover", name="Hover", state="hover"),
                ComponentVariant(variant_id="primary_disabled", name="Disabled", state="disabled", properties={"opacity": 0.5}),
                ComponentVariant(variant_id="primary_loading", name="Loading Spinner", state="loading"),
            ]
        ))

        # 2. Secondary Button
        registry.register(ComponentDefinition(
            component_id="cmp_btn_secondary",
            name="Secondary Action Button",
            type=ComponentType.BUTTON,
            description="Subtle outline button for secondary dismissive or navigation actions.",
            default_width=120,
            default_height=44 if platform == "mobile" else 36,
            auto_layout_direction="horizontal",
            padding_x=16,
            padding_y=10,
            gap=8,
            corner_radius=8,
            bg_token_ref="surface",
            text_token_ref="text_primary",
            border_token_ref="border_subtle",
            variants=[
                ComponentVariant(variant_id="sec_default", name="Default", state="default"),
                ComponentVariant(variant_id="sec_hover", name="Hover", state="hover"),
            ]
        ))

        # 3. Icon Button
        registry.register(ComponentDefinition(
            component_id="cmp_icon_button",
            name="Icon Button",
            type=ComponentType.ICON_BUTTON,
            description="Compact square target for filters, back navigation, or bookmarking.",
            default_width=40,
            default_height=40,
            auto_layout_direction="horizontal",
            padding_x=8,
            padding_y=8,
            gap=0,
            corner_radius=8,
            bg_token_ref="surface",
            text_token_ref="text_primary"
        ))

        # 4. Search Input Bar
        registry.register(ComponentDefinition(
            component_id="cmp_search_bar",
            name="Search Input Bar",
            type=ComponentType.SEARCH_BAR,
            description="Input field with magnifying glass icon and clear button.",
            default_width=361 if platform == "mobile" else 320,
            default_height=44,
            auto_layout_direction="horizontal",
            padding_x=14,
            padding_y=10,
            gap=10,
            corner_radius=10,
            bg_token_ref="surface",
            text_token_ref="text_primary",
            border_token_ref="border_subtle"
        ))

        # 5. Form Text Input
        registry.register(ComponentDefinition(
            component_id="cmp_input_field",
            name="Text Input Field",
            type=ComponentType.INPUT,
            description="Standard labeled input with inline validation message slot.",
            default_width=361 if platform == "mobile" else 280,
            default_height=52,
            auto_layout_direction="vertical",
            padding_x=12,
            padding_y=8,
            gap=4,
            corner_radius=8,
            bg_token_ref="surface",
            text_token_ref="text_primary",
            border_token_ref="border_subtle"
        ))

        # 6. Entity Card (Restaurant or Task Card)
        registry.register(ComponentDefinition(
            component_id="cmp_entity_card",
            name="Entity Content Card",
            type=ComponentType.CARD,
            description="Primary display card showcasing preview metadata, pricing/status, and title.",
            default_width=361 if platform == "mobile" else 290,
            default_height=180 if platform == "mobile" else 140,
            auto_layout_direction="vertical",
            padding_x=16,
            padding_y=16,
            gap=12,
            corner_radius=12,
            bg_token_ref="surface",
            text_token_ref="text_primary",
            border_token_ref="border_subtle"
        ))

        # 7. Navigation Bar (Bottom Tabs for mobile, Sidebar for desktop)
        nav_type = ComponentType.NAVBAR if platform == "mobile" else ComponentType.SIDEBAR
        registry.register(ComponentDefinition(
            component_id="cmp_global_nav",
            name="Global Navigation Container",
            type=nav_type,
            description="Persistent navigation affordance supporting primary route changes.",
            default_width=393 if platform == "mobile" else 240,
            default_height=80 if platform == "mobile" else 900,
            auto_layout_direction="horizontal" if platform == "mobile" else "vertical",
            padding_x=16,
            padding_y=12,
            gap=24 if platform == "mobile" else 16,
            corner_radius=0,
            bg_token_ref="surface",
            text_token_ref="text_secondary",
            border_token_ref="border_subtle"
        ))

        # 8. Status Badge / Tag
        registry.register(ComponentDefinition(
            component_id="cmp_status_badge",
            name="Semantic Status Badge",
            type=ComponentType.BADGE,
            description="Micro visual indicator for status: In Progress, Urgent, Discount, Under $10.",
            default_width=72,
            default_height=24,
            auto_layout_direction="horizontal",
            padding_x=8,
            padding_y=4,
            gap=4,
            corner_radius=9999,
            bg_token_ref="accent",
            text_token_ref="text_primary"
        ))

        # 9. Avatar
        registry.register(ComponentDefinition(
            component_id="cmp_user_avatar",
            name="User Avatar",
            type=ComponentType.AVATAR,
            description="Circular profile picture or 2-letter fallback initials.",
            default_width=36,
            default_height=36,
            auto_layout_direction="horizontal",
            padding_x=0,
            padding_y=0,
            gap=0,
            corner_radius=9999,
            bg_token_ref="secondary",
            text_token_ref="text_on_secondary"
        ))

        # 10. Modal / Bottom Sheet
        sheet_type = ComponentType.BOTTOM_SHEET if platform == "mobile" else ComponentType.MODAL
        registry.register(ComponentDefinition(
            component_id="cmp_overlay_container",
            name="Focused Overlay Container",
            type=sheet_type,
            description="Contextual sheet or dialog for task creation, dish customization, or checkout.",
            default_width=393 if platform == "mobile" else 560,
            default_height=450,
            auto_layout_direction="vertical",
            padding_x=24,
            padding_y=20,
            gap=16,
            corner_radius=20 if platform == "mobile" else 12,
            bg_token_ref="surface_elevated",
            text_token_ref="text_primary"
        ))

        # 11. Empty State
        registry.register(ComponentDefinition(
            component_id="cmp_empty_state",
            name="Zero-Data Empty State",
            type=ComponentType.EMPTY_STATE,
            description="Friendly illustration, helpful explanation, and prominent recovery CTA.",
            default_width=340,
            default_height=200,
            auto_layout_direction="vertical",
            padding_x=20,
            padding_y=24,
            gap=12,
            corner_radius=12,
            bg_token_ref="surface",
            text_token_ref="text_muted"
        ))

        # 12. Error State / Banner
        registry.register(ComponentDefinition(
            component_id="cmp_error_banner",
            name="Inline Error Recovery Banner",
            type=ComponentType.ERROR_STATE,
            description="Alert banner highlighting failed operation with explicit retry trigger.",
            default_width=361 if platform == "mobile" else 500,
            default_height=56,
            auto_layout_direction="horizontal",
            padding_x=16,
            padding_y=12,
            gap=12,
            corner_radius=8,
            bg_token_ref="surface",
            text_token_ref="error",
            border_token_ref="error"
        ))

        # 13. Data Table (for Desktop SaaS)
        if platform in ["desktop", "web"]:
            registry.register(ComponentDefinition(
                component_id="cmp_data_table",
                name="Sortable Data Table",
                type=ComponentType.TABLE,
                description="Dense scannable grid supporting sorting, selection, and status chips.",
                default_width=980,
                default_height=420,
                auto_layout_direction="vertical",
                padding_x=0,
                padding_y=0,
                gap=0,
                corner_radius=8,
                bg_token_ref="surface",
                text_token_ref="text_primary",
                border_token_ref="border_subtle"
            ))

        return registry
