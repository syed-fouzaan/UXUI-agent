"""
End-to-End Integration Tests across TWO completely distinct product domains:
1. Campus Food Delivery Mobile App (Section 35)
2. Developer Project Management SaaS (Section 36)
Proves generic domain resilience and architectural robustness.
"""

import pytest
from azia.azia_core.orchestrator import AutonomousDesignPipeline


def test_domain_1_food_delivery_e2e():
    pipeline = AutonomousDesignPipeline()
    req = (
        "Build a modern food delivery app for college students. "
        "Students should discover nearby restaurants, search food, "
        "order food, pay, and track delivery. The experience should be fast, affordable and simple."
    )

    spec, ops, canvas, summary = pipeline.design_product(
        requirement=req,
        platform="mobile"
    )

    assert spec.metadata.platform == "mobile"
    assert "food" in spec.metadata.product_category.lower()
    assert len(spec.screens) >= 6
    assert len(spec.prototype.connections) >= 4
    assert summary["qa_score"] >= 90
    assert summary["status"] == "SUCCESS_PRODUCTION_READY"

    # Verify key screens exist
    screen_ids = [s.screen_id for s in spec.screens]
    assert "scr_home" in screen_ids
    assert "scr_search" in screen_ids
    assert "scr_restaurant_detail" in screen_ids
    assert "scr_cart" in screen_ids
    assert "scr_checkout" in screen_ids
    assert "scr_order_tracking" in screen_ids


def test_domain_2_saas_project_management_e2e():
    pipeline = AutonomousDesignPipeline()
    req = (
        "Build a project management SaaS for small engineering teams. "
        "Teams should create projects, manage tasks, assign work, track progress, and see project status."
    )

    spec, ops, canvas, summary = pipeline.design_product(
        requirement=req,
        platform="desktop"
    )

    assert spec.metadata.platform == "desktop"
    assert "project" in spec.metadata.product_category.lower() or "saas" in spec.metadata.product_category.lower()
    assert len(spec.screens) >= 3
    assert summary["qa_score"] >= 90
    assert summary["status"] == "SUCCESS_PRODUCTION_READY"

    # Verify completely different screen inventory
    screen_ids = [s.screen_id for s in spec.screens]
    assert "scr_dashboard" in screen_ids
    assert "scr_kanban_board" in screen_ids
    assert "scr_task_detail" in screen_ids
    assert "scr_analytics" in screen_ids

    # Verify sidebar navigation pattern for desktop SaaS
    assert spec.information_architecture.navigation_model.pattern == "left_sidebar"
