"""
Unit tests for OperationPlanner, VirtualFigmaCanvas, and Non-Destructive Rollback.
"""

import pytest
from azia.azia_core.orchestrator import AutonomousDesignPipeline
from azia.azia_core.renderer.virtual_canvas import VirtualFigmaCanvas
from azia.azia_core.models.operations import FigmaOperationType


def test_operation_planner_and_virtual_canvas():
    pipeline = AutonomousDesignPipeline()
    spec, ops, canvas, summary = pipeline.design_product(
        "Build a modern food delivery app for college students"
    )

    assert len(ops) > 20
    # Verify operation ordering: page and sections come before nested frames
    op_types = [op.op_type for op in ops]
    assert op_types[0] == FigmaOperationType.CREATE_PAGE
    assert FigmaOperationType.CREATE_SECTION in op_types
    assert FigmaOperationType.CREATE_SCREEN in op_types

    # Verify virtual canvas node creation
    managed_nodes = canvas.find_nodes_by_ownership("autonomous-design-mcp")
    assert len(managed_nodes) > 10

    # Test non-destructive rollback
    gen_id = summary["generation_id"]
    deleted = canvas.rollback_generation(gen_id)
    assert deleted > 0
