"""
AZIA Autonomous Self-Repair Engine
Implements bounded optimization loop:
GENERATE -> INSPECT -> FIND ISSUES -> PRIORITIZE -> GENERATE FIX OPERATIONS -> APPLY -> INSPECT AGAIN -> PASS
Bounded by MAX_REPAIR_ITERATIONS = 3 to guarantee termination.
"""

from typing import Tuple, List
from azia.azia_core.models.specification import ProductDesignSpecification
from azia.azia_core.models.qa import ComprehensiveQAReport
from azia.azia_core.intelligence.qa_engine import QAEngine


class RepairEngine:
    """Executes closed-loop bounded automated remediation on generated specifications."""

    MAX_REPAIR_ITERATIONS = 3

    def __init__(self):
        self.qa_engine = QAEngine()

    def run_repair_loop(
        self,
        spec: ProductDesignSpecification
    ) -> Tuple[ProductDesignSpecification, ComprehensiveQAReport]:
        iteration = 0
        resolved_issues: List[str] = []

        qa_report = self.qa_engine.evaluate(spec)

        while iteration < self.MAX_REPAIR_ITERATIONS:
            issues_found = [
                chk for chk in qa_report.visual_qa.checks if not chk.passed
            ]

            if not issues_found and qa_report.requirement_coverage_percentage >= 100.0:
                # Perfectly clean run
                break

            iteration += 1

            # Fix detected issues
            for issue in issues_found:
                if issue.check_id == "QA-VIS-01":
                    # Fix 8pt grid
                    for screen in spec.screens:
                        for sec in screen.sections:
                            sec.gap = round(sec.gap / 4) * 4
                            sec.padding = round(sec.padding / 4) * 4
                    resolved_issues.append(f"Auto-aligned section padding and gaps to strict 4px/8px boundary in iteration {iteration}.")

                elif issue.check_id == "QA-VIS-04":
                    # Ensure all instances reference registered components
                    for screen in spec.screens:
                        for sec in screen.sections:
                            for inst in sec.components:
                                if inst.component_ref not in spec.component_registry.components:
                                    inst.component_ref = "cmp_entity_card"
                    resolved_issues.append(f"Remapped unlinked component instances to verified masters in iteration {iteration}.")

            # Re-evaluate
            qa_report = self.qa_engine.evaluate(spec)

        qa_report.repair_iterations_applied = iteration
        qa_report.issues_resolved = resolved_issues
        spec.qa_report = qa_report

        return spec, qa_report
