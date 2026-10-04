"""
Unit tests for DesignSystemEngine, ComponentEngine, and ScreenEngine.
"""

import pytest
from azia.azia_core.intelligence.requirement_engine import RequirementEngine
from azia.azia_core.intelligence.design_system_engine import DesignSystemEngine
from azia.azia_core.intelligence.component_engine import ComponentEngine
from azia.azia_core.intelligence.screen_engine import ScreenEngine


def test_design_system_tokens_and_accessibility():
    req_engine = RequirementEngine()
    ds_engine = DesignSystemEngine()

    analysis = req_engine.analyze("Build a modern food delivery app for college students", platform_hint="mobile")
    tokens = ds_engine.synthesize(analysis)

    # Check color tokens
    assert tokens.colors.primary.hex.startswith("#")
    assert tokens.colors.background.hex.startswith("#")
    assert tokens.colors.text_primary.wcag_aa_compliant is True
    assert tokens.colors.primary.contrast_ratio_on_bg >= 4.5

    # Check 8pt grid spacing scale
    assert tokens.spacing.sm == 8
    assert tokens.spacing.md == 16
    assert tokens.spacing.lg == 24
    assert tokens.spacing.xl == 32


def test_component_engine_reusability():
    req_engine = RequirementEngine()
    comp_engine = ComponentEngine()

    analysis = req_engine.analyze("Build a modern food delivery app for college students")
    registry = comp_engine.build_registry(analysis)

    assert "cmp_btn_primary" in registry.components
    assert "cmp_search_bar" in registry.components
    assert "cmp_entity_card" in registry.components
    assert "cmp_global_nav" in registry.components

    btn = registry.get("cmp_btn_primary")
    assert btn.auto_layout_direction == "horizontal"
    assert len(btn.variants) >= 2


def test_screen_engine_auto_layout_and_states():
    req_engine = RequirementEngine()
    screen_engine = ScreenEngine()

    analysis = req_engine.analyze("Build a modern food delivery app for college students")
    screens = screen_engine.plan_screens(analysis)

    assert len(screens) >= 5
    for s in screens:
        assert s.screen_id.startswith("scr_")
        assert s.layout.width > 0
        assert s.layout.height > 0
        assert s.primary_cta != ""
        assert len(s.sections) >= 1
