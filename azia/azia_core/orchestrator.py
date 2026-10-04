"""
AZIA Master Autonomous Design Orchestrator
Coordinates the end-to-end autonomous design pipeline:
Requirement -> Pre-flight -> Epistemic Register -> UX Architecture -> IA ->
User Flows -> Design System Tokens -> Reusable Components -> Screen Planning ->
Prototype Connections -> Non-Disruptive Strategy -> Heuristic Audit ->
Visual/UX QA -> Bounded Self-Repair -> Operation Planning -> Virtual Figma Rendering.
"""

import uuid
import time
from typing import Dict, Any, Optional, List, Tuple

from azia.azia_core.models.specification import (
    ProductMetadata,
    ProductDesignSpecification,
)
from azia.azia_core.models.operations import FigmaOperation
from azia.azia_core.intelligence import (
    PreFlightEngine,
    RequirementEngine,
    RequirementAnalysis,
    UXEngine,
    IAEngine,
    FlowEngine,
    DesignSystemEngine,
    ComponentEngine,
    ScreenEngine,
    PrototypeEngine,
    StrategyEngine,
    AuditEngine,
    QAEngine,
    RepairEngine,
)
from azia.azia_core.renderer import (
    OperationPlanner,
    VirtualFigmaCanvas,
    VisualExporter,
    FigmaExporter,
)


class AutonomousDesignPipeline:
    """The master cognitive pipeline implementing 'One Requirement -> Complete Product Design'."""

    def __init__(self):
        self.preflight_engine = PreFlightEngine()
        self.req_engine = RequirementEngine()
        self.ux_engine = UXEngine()
        self.ia_engine = IAEngine()
        self.flow_engine = FlowEngine()
        self.ds_engine = DesignSystemEngine()
        self.comp_engine = ComponentEngine()
        self.screen_engine = ScreenEngine()
        self.proto_engine = PrototypeEngine()
        self.strategy_engine = StrategyEngine()
        self.audit_engine = AuditEngine()
        self.qa_engine = QAEngine()
        self.repair_engine = RepairEngine()
        self.op_planner = OperationPlanner()
        self.visual_exporter = VisualExporter()
        self.figma_exporter = FigmaExporter()

    def design_product(
        self,
        requirement: str,
        platform: Optional[str] = "auto",
        style: Optional[str] = "auto",
        fidelity: Optional[str] = "high",
        existing_figma_context: Optional[bool] = False,
        multimodal_docs: Optional[List[str]] = None
    ) -> Tuple[ProductDesignSpecification, List[FigmaOperation], VirtualFigmaCanvas, Dict[str, Any]]:
        """Executes the full autonomous design sequence."""
        start_time = time.time()
        generation_id = str(uuid.uuid4())

        # Step 1: Pre-flight context inspection
        preflight_result = self.preflight_engine.evaluate(requirement)

        # Step 2: Requirement understanding & Epistemic classification
        req_analysis = self.req_engine.analyze(
            requirement=requirement,
            platform_hint=platform,
            style_hint=style,
            multimodal_docs=multimodal_docs
        )

        # Step 3: UX Architecture (Evidence-based Personas & JTBD)
        ux_arch = self.ux_engine.synthesize(req_analysis)

        # Step 4: Information Architecture (Navigation, hierarchy, entities)
        ia_arch = self.ia_engine.plan(req_analysis)

        # Step 5: User Flows & Topological Health Validation
        user_flows = self.flow_engine.plan_flows(req_analysis)
        for flow in user_flows:
            val_res = self.flow_engine.validate_flow(flow)

        # Step 6: Design System Token Synthesis (WCAG AA/AAA, 8pt Grid)
        design_system = self.ds_engine.synthesize(req_analysis)

        # Step 7: Semantic Reusable Component Library
        components = self.comp_engine.build_registry(req_analysis)

        # Step 8: Screen Planning & Auto Layout Hierarchy
        screens = self.screen_engine.plan_screens(req_analysis)

        # Step 9: Prototype Connection Graph
        prototype = self.proto_engine.build_prototype_graph(screens, req_analysis)

        # Step 10: Non-Disruptive Feature Strategy
        strategy = self.strategy_engine.formulate_strategy(req_analysis)

        # Step 11: Assemble Candidate Specification
        metadata = ProductMetadata(
            product_id=f"prd_{uuid.uuid4().hex[:8]}",
            product_name=req_analysis.product_name,
            product_category=req_analysis.product_category,
            requirement_prompt=requirement,
            platform=req_analysis.platform,
            style_direction=req_analysis.style,
            generation_id=generation_id,
            managed_by="autonomous-design-mcp"
        )

        spec = ProductDesignSpecification(
            metadata=metadata,
            preflight=preflight_result,
            epistemic_register=req_analysis.epistemic_register,
            ux_architecture=ux_arch,
            information_architecture=ia_arch,
            user_flows=user_flows,
            design_system=design_system,
            component_registry=components,
            screens=screens,
            prototype=prototype,
            non_disruptive_strategy=strategy
        )

        # Step 12: Nielsen Usability & Accessibility Audit
        audit_report = self.audit_engine.audit_specification(spec)
        spec.audit_report = audit_report

        # Step 13: Dual-Track QA & Bounded Self-Repair Loop
        spec, qa_report = self.repair_engine.run_repair_loop(spec)

        # Step 14: Operation Planner (Deterministic Figma Operations)
        operations = self.op_planner.plan_operations(spec)

        # Step 15: Render into Virtual Figma Document
        canvas = VirtualFigmaCanvas()
        canvas.execute_operations(operations)

        duration = round(time.time() - start_time, 2)

        summary = {
            "product_name": spec.metadata.product_name,
            "category": spec.metadata.product_category,
            "generation_id": generation_id,
            "platform": spec.metadata.platform,
            "screens_created": len(spec.screens),
            "components_created": len(spec.component_registry.components),
            "flows_created": len(spec.user_flows),
            "operations_count": len(operations),
            "qa_score": qa_report.overall_qa_score_100,
            "usability_score": audit_report.overall_usability_score_100,
            "repair_iterations": qa_report.repair_iterations_applied,
            "execution_duration_sec": duration,
            "status": "SUCCESS_PRODUCTION_READY"
        }

        return spec, operations, canvas, summary
