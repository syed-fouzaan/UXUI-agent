"""
Unit tests for UXEngine, IAEngine, and FlowEngine.
"""

import pytest
from azia.azia_core.intelligence.requirement_engine import RequirementEngine
from azia.azia_core.intelligence.ux_engine import UXEngine
from azia.azia_core.intelligence.ia_engine import IAEngine
from azia.azia_core.intelligence.flow_engine import FlowEngine


def test_ux_engine_synthesizes_personas_and_jtbd():
    req_engine = RequirementEngine()
    ux_engine = UXEngine()

    analysis = req_engine.analyze("Build a modern food delivery app for college students")
    ux_arch = ux_engine.synthesize(analysis)

    assert len(ux_arch.personas) >= 2
    for p in ux_arch.personas:
        assert p.id.startswith("PER-")
        assert len(p.core_needs) > 0
        assert len(p.pain_points) > 0
        assert p.context_of_use != ""

    assert len(ux_arch.jtbd_list) >= 2
    for j in ux_arch.jtbd_list:
        assert j.situation.startswith("When")
        assert j.motivation.startswith("I want to")
        assert j.expected_outcome.startswith("So I can")


def test_ia_engine_navigation_and_entities():
    req_engine = RequirementEngine()
    ia_engine = IAEngine()

    analysis = req_engine.analyze("Build a modern food delivery app for college students")
    ia = ia_engine.plan(analysis)

    assert ia.navigation_model.pattern in ["bottom_tabs", "left_sidebar"]
    assert len(ia.navigation_model.primary_items) >= 3
    assert len(ia.screen_groups) >= 2
    assert len(ia.entity_relationships) >= 2


def test_flow_engine_topological_health():
    req_engine = RequirementEngine()
    flow_engine = FlowEngine()

    analysis = req_engine.analyze("Build a modern food delivery app for college students")
    flows = flow_engine.plan_flows(analysis)

    assert len(flows) >= 1
    primary_flow = flows[0]
    assert len(primary_flow.nodes) >= 5
    assert len(primary_flow.edges) >= 4

    validation = flow_engine.validate_flow(primary_flow)
    assert validation.is_valid is True
    assert len(validation.dead_ends) == 0
    assert len(validation.unreachable_nodes) == 0
