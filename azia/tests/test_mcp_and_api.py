"""
Tests for AZIA MCP Server Tools and REST API Server
Verifies simulation, code export, and design system ingestion capabilities.
"""

import json
import pytest
from azia.mcp_server import (
    design_product,
    run_usability_simulation,
    export_production_code,
    ingest_design_system,
    preflight_check
)
from azia.api_server import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_mcp_preflight():
    res = json.loads(preflight_check("Design a campus food delivery app"))
    assert "context_score" in res
    assert res["context_score"] > 0


def test_mcp_design_and_simulation():
    # 1. Generate design
    design_res = json.loads(design_product(
        requirement="Quick order pizza for hungry late-night students",
        platform="mobile",
        fidelity="high"
    ))
    assert design_res["status"] == "SUCCESS"
    gen_id = design_res["generation_id"]

    # 2. Run simulation tool
    sim_res = json.loads(run_usability_simulation(gen_id))
    assert "overall_funnel_conversion_rate" in sim_res
    assert len(sim_res["screen_heatmaps"]) > 0
    assert len(sim_res["funnel_steps"]) > 0

    # 3. Export production code tool
    react_code = json.loads(export_production_code(gen_id, framework="react"))
    assert react_code["framework"] == "REACT_TAILWIND"
    assert len(react_code["files"]) > 0

    swift_code = json.loads(export_production_code(gen_id, framework="swiftui"))
    assert swift_code["framework"] == "SWIFTUI"
    assert len(swift_code["files"]) > 0


def test_mcp_design_system_ingest():
    sample_tokens = {
        "color": {
            "primary": {"value": "#4F46E5", "type": "color"},
            "accent": {"value": "#10B981", "type": "color"}
        }
    }
    ingest_res = json.loads(ingest_design_system("figma_tokens", json.dumps(sample_tokens)))
    assert ingest_res["source_format"] == "FIGMA_TOKENS_STUDIO"
    assert ingest_res["total_tokens_imported"] >= 2


def test_api_server_endpoints():
    # Health endpoint
    health_resp = client.get("/health")
    assert health_resp.status_code == 200
    assert health_resp.json()["status"] == "ok"

    # Spar endpoint
    spar_resp = client.post("/api/spar", json={"query": "Why use progressive disclosure?"})
    assert spar_resp.status_code == 200
    assert "critique" in spar_resp.json()

    # Code handoff endpoint
    code_resp = client.post("/api/code-handoff", json={"framework": "tokens"})
    assert code_resp.status_code == 200
    assert "tokens.json" in code_resp.json()["filename"]
