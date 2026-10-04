"""
Unit tests for SimulationEngine (Synthetic Usability & Visual Attention Heatmaps).
"""

import pytest
from azia.azia_core.orchestrator import AutonomousDesignPipeline
from azia.azia_core.intelligence.simulation_engine import SimulationEngine


def test_synthetic_usability_simulation():
    pipeline = AutonomousDesignPipeline()
    sim_engine = SimulationEngine()

    spec, _, _, _ = pipeline.design_product(
        "Build a modern food delivery app for college students"
    )

    report = sim_engine.run_simulation(spec, total_sessions=500)

    assert report.total_simulated_sessions == 500
    assert 0.0 < report.overall_funnel_conversion_rate <= 100.0
    assert report.avg_time_to_completion_seconds > 0.0
    assert len(report.funnel_steps) == len(spec.screens)

    # Check first step starts with high retention and declines monotonically
    retentions = [s.retained_percentage for s in report.funnel_steps]
    assert all(x >= y for x, y in zip(retentions, retentions[1:]))

    # Check visual saliency heatmaps
    assert len(report.screen_heatmaps) == len(spec.screens)
    for hm in report.screen_heatmaps:
        assert len(hm.fixations) >= 3
        # Ensure noticeability is high for focal elements
        assert any(f.noticeability_percentage >= 90 for f in hm.fixations)
