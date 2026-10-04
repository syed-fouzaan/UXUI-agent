"""
AZIA Semantic Figma Operation Planner
Transforms a validated ProductDesignSpecification into an ordered, deterministic sequence
of semantic Figma operations.
"""

from typing import List, Dict, Any
from azia.azia_core.models.specification import ProductDesignSpecification
from azia.azia_core.models.operations import (
    FigmaOperation,
    FigmaOperationType,
)


class OperationPlanner:
    """Plans ordered semantic operations ensuring dependencies (pages, styles, components) are created first."""

    def plan_operations(self, spec: ProductDesignSpecification) -> List[FigmaOperation]:
        ops: List[FigmaOperation] = []
        gen_id = spec.metadata.generation_id
        prod_id = spec.metadata.product_id
        managed_by = spec.metadata.managed_by
        op_seq = 1

        def add_op(op_type: FigmaOperationType, target_id: str, name: str, payload: Dict[str, Any], parent_id: str = None):
            nonlocal op_seq
            ops.append(
                FigmaOperation(
                    op_id=f"op_{op_seq:04d}",
                    op_type=op_type,
                    target_id=target_id,
                    parent_id=parent_id,
                    name=name,
                    payload=payload,
                    managed_by=managed_by,
                    generation_id=gen_id
                )
            )
            op_seq += 1

        # 1. Create Main Document Page
        page_id = f"page_{prod_id}"
        add_op(
            FigmaOperationType.CREATE_PAGE,
            target_id=page_id,
            name=f"✨ {spec.metadata.product_name} • Master Design System & Flows",
            payload={"product_id": prod_id, "category": spec.metadata.product_category}
        )

        # 2. Create FigJam / UX Architecture Section
        sec_ux_id = f"sec_ux_arch_{prod_id}"
        add_op(
            FigmaOperationType.CREATE_SECTION,
            target_id=sec_ux_id,
            parent_id=page_id,
            name="1. UX Architecture & Discovery Board",
            payload={"x": 0, "y": 0, "width": 1600, "height": 900}
        )

        # 3. Create Persona & Assumption Sticky Notes on UX Board
        sticky_x = 50
        for i, persona in enumerate(spec.ux_architecture.personas):
            add_op(
                FigmaOperationType.CREATE_STICKY_NOTE,
                target_id=f"sticky_persona_{persona.id}",
                parent_id=sec_ux_id,
                name=f"Persona: {persona.name}",
                payload={
                    "x": sticky_x,
                    "y": 100,
                    "color": "BLUE",
                    "content": f"👤 {persona.name}\nRole: {persona.role}\nGoal: {persona.primary_goal}\nContext: {persona.context_of_use}"
                }
            )
            sticky_x += 320

        # Assumptions Sticky Notes
        asm_x = 50
        for i, asm in enumerate(spec.epistemic_register.explicit_assumptions):
            add_op(
                FigmaOperationType.CREATE_STICKY_NOTE,
                target_id=f"sticky_asm_{asm.id}",
                parent_id=sec_ux_id,
                name=f"Assumption: {asm.id}",
                payload={
                    "x": asm_x,
                    "y": 420,
                    "color": "YELLOW",
                    "content": f"💡 ASSUMPTION ({asm.confidence.value})\n{asm.statement}\nValidation: {asm.recommended_validation_method}"
                }
            )
            asm_x += 320

        # 4. Create Reusable Component Section & Components
        sec_comp_id = f"sec_components_{prod_id}"
        add_op(
            FigmaOperationType.CREATE_SECTION,
            target_id=sec_comp_id,
            parent_id=page_id,
            name="2. Design System & Master Components",
            payload={"x": 1800, "y": 0, "width": 1400, "height": 900}
        )

        comp_y = 100
        for comp_id, comp_def in spec.component_registry.components.items():
            add_op(
                FigmaOperationType.CREATE_COMPONENT,
                target_id=comp_id,
                parent_id=sec_comp_id,
                name=comp_def.name,
                payload={
                    "type": comp_def.type.value,
                    "width": comp_def.default_width,
                    "height": comp_def.default_height,
                    "direction": comp_def.auto_layout_direction,
                    "padding_x": comp_def.padding_x,
                    "padding_y": comp_def.padding_y,
                    "gap": comp_def.gap,
                    "radius": comp_def.corner_radius,
                    "bg_token": comp_def.bg_token_ref,
                    "text_token": comp_def.text_token_ref,
                    "y": comp_y
                }
            )
            comp_y += comp_def.default_height + 40

        # 5. Create High-Fidelity UI Screens Section & Screens
        sec_screens_id = f"sec_screens_{prod_id}"
        add_op(
            FigmaOperationType.CREATE_SECTION,
            target_id=sec_screens_id,
            parent_id=page_id,
            name="3. Interactive Connected Product Screens",
            payload={"x": 3400, "y": 0, "width": 3600, "height": 1100}
        )

        screen_x = 3500
        screen_gap = 80

        for screen in spec.screens:
            # Create Screen Frame with Auto Layout
            add_op(
                FigmaOperationType.CREATE_SCREEN,
                target_id=screen.screen_id,
                parent_id=sec_screens_id,
                name=f"{screen.screen_id}: {screen.screen_name}",
                payload={
                    "x": screen_x,
                    "y": 100,
                    "width": screen.layout.width,
                    "height": screen.layout.height,
                    "direction": screen.layout.direction,
                    "padding_top": screen.layout.padding_top,
                    "padding_bottom": screen.layout.padding_bottom,
                    "padding_x": screen.layout.padding_left,
                    "gap": screen.layout.gap,
                    "bg_hex": spec.design_system.colors.background.hex,
                    "scrollable": screen.layout.scrollable
                }
            )

            # Add Screen Sections & Components
            for sec in screen.sections:
                sec_container_id = f"sec_{screen.screen_id}_{sec.section_id}"
                add_op(
                    FigmaOperationType.CREATE_AUTO_LAYOUT,
                    target_id=sec_container_id,
                    parent_id=screen.screen_id,
                    name=sec.title,
                    payload={
                        "direction": sec.direction,
                        "gap": sec.gap,
                        "padding": sec.padding,
                        "layout_mode": sec.layout_mode
                    }
                )

                for cmp_inst in sec.components:
                    add_op(
                        FigmaOperationType.CREATE_INSTANCE,
                        target_id=f"inst_{screen.screen_id}_{cmp_inst.instance_id}",
                        parent_id=sec_container_id,
                        name=cmp_inst.name,
                        payload={
                            "master_component_id": cmp_inst.component_ref,
                            "content_data": cmp_inst.content_data,
                            "interactive_target_screen_id": cmp_inst.interactive_target_screen_id
                        }
                    )

            screen_x += screen.layout.width + screen_gap

        # 6. Create Interactive Prototype Connections
        for conn in spec.prototype.connections:
            add_op(
                FigmaOperationType.CONNECT_PROTOTYPE,
                target_id=conn.id,
                name=f"Link: {conn.source_screen_id} -> {conn.target_screen_id}",
                payload={
                    "source_screen_id": conn.source_screen_id,
                    "target_screen_id": conn.target_screen_id,
                    "source_element_id": conn.source_element_id,
                    "trigger": conn.trigger.value,
                    "animation": conn.animation.value,
                    "duration_ms": conn.duration_ms
                }
            )

        return ops
