"""
Unit tests for QAEngine, AuditEngine, and RepairEngine.
"""

import pytest
from azia.azia_core.orchestrator import AutonomousDesignPipeline
from azia.azia_core.intelligence.qa_engine import QAEngine
from azia.azia_core.intelligence.audit_engine import AuditEngine
from azia.azia_core.intelligence.repair_engine import RepairEngine


def test_qa_and_audit_reports():
    pipeline = AutonomousDesignPipeline()
    spec, ops, canvas, summary = pipeline.design_product(
        "Build a modern food delivery app for college students"
    )

    # QA Report Checks
    assert spec.qa_report is not None
    assert spec.qa_report.overall_qa_score_100 >= 90
    assert spec.qa_report.requirement_coverage_percentage == 100.0
    assert spec.qa_report.visual_qa.grid_alignment_passed is True

    # Audit Report Checks
    assert spec.audit_report is not None
    assert spec.audit_report.overall_usability_score_100 >= 75
    assert len(spec.audit_report.findings) >= 1
    for f in spec.audit_report.findings:
        assert f.problem != ""
        assert f.recommendation != ""
        assert f.ux_principle != ""


def test_bounded_self_repair_loop():
    repair_engine = RepairEngine()
    pipeline = AutonomousDesignPipeline()
    spec, _, _, _ = pipeline.design_product(
        "Build a modern food delivery app for college students"
    )

    # Artificially misalign a section gap to test repair detection
    spec.screens[0].sections[0].gap = 7  # Not multiple of 4

    repaired_spec, qa_report = repair_engine.run_repair_loop(spec)
    assert repaired_spec.screens[0].sections[0].gap % 4 == 0
    assert qa_report.repair_iterations_applied <= 3
