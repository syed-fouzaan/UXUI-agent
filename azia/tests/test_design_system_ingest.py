"""
Unit tests for DesignSystemIngestEngine (Figma Tokens Studio, CSS variables).
"""

import json
import pytest
from azia.azia_core.intelligence.design_system_ingest import DesignSystemIngestEngine
from azia.azia_core.models.ds_ingest import DesignSystemSourceFormat


def test_figma_tokens_studio_ingestion():
    engine = DesignSystemIngestEngine()
    sample_tokens = {
        "name": "Acme Enterprise Design System",
        "global": {
            "colors": {
                "brand": {"primary": {"value": "#0052CC", "type": "color"}},
                "neutral": {"background": {"value": "#F4F5F7", "type": "color"}}
            },
            "spacing": {
                "sm": {"value": "8px", "type": "spacing"},
                "md": {"value": "16px", "type": "spacing"}
            }
        }
    }

    result = engine.ingest_figma_tokens(json.dumps(sample_tokens))

    assert result.success is True
    assert result.source_format == DesignSystemSourceFormat.FIGMA_TOKENS_STUDIO
    assert result.color_tokens_count >= 2
    assert result.spacing_tokens_count >= 2
    assert len(result.component_mappings) >= 1


def test_css_variables_ingestion():
    engine = DesignSystemIngestEngine()
    css = """
    :root {
      --primary-color: #2563EB;
      --surface-color: #FFFFFF;
      --spacing-unit: 8px;
    }
    """

    result = engine.ingest_css_variables(css)

    assert result.success is True
    assert result.source_format == DesignSystemSourceFormat.CSS_VARIABLES
    assert result.total_tokens_imported >= 3
    assert result.color_tokens_count >= 2
