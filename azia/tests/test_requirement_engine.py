"""
Unit tests for RequirementEngine & Epistemic Taxonomy.
"""

import pytest
from azia.azia_core.intelligence.requirement_engine import RequirementEngine
from azia.azia_core.models.taxonomy import EpistemicStatus, ConfidenceLevel


def test_requirement_engine_food_delivery():
    engine = RequirementEngine()
    req = "Build a modern food delivery app for college students. Students should discover nearby restaurants, search food, order food, pay, and track delivery."
    analysis = engine.analyze(req)

    assert "food" in analysis.product_category.lower()
    assert analysis.platform == "mobile"
    assert len(analysis.target_users) >= 1
    assert len(analysis.core_tasks) >= 4
    assert len(analysis.entities) >= 4
    assert len(analysis.actions) >= 4

    # Verify epistemic status classification
    facts = analysis.epistemic_register.confirmed_facts
    assert len(facts) >= 1
    assert facts[0].confidence == ConfidenceLevel.HIGH

    assumptions = analysis.epistemic_register.explicit_assumptions
    assert len(assumptions) >= 1
    for asm in assumptions:
        assert asm.statement != ""
        assert asm.recommended_validation_method != ""


def test_requirement_engine_saas_pm():
    engine = RequirementEngine()
    req = "Build a project management SaaS for small engineering teams. Teams should create projects, manage tasks, assign work, track progress, and see project status."
    analysis = engine.analyze(req)

    assert "project" in analysis.product_category.lower() or "saas" in analysis.product_category.lower()
    assert analysis.platform in ["desktop", "web"]
    assert len(analysis.entities) >= 3
    assert "Task" in analysis.entities or "Project" in analysis.entities
