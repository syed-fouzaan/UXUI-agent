"""
AZIA Autonomous Figma Product Design MCP Server
Exposes high-level autonomous design tools and Socratic sparring interfaces
over standard Model Context Protocol (MCP).
"""

import sys
import os
import json
from typing import Optional, Dict, Any, List

# Ensure azia package is accessible
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from mcp.server.fastmcp import FastMCP
from azia.azia_core.orchestrator import AutonomousDesignPipeline
from azia.azia_core.intelligence.mentor_sparring import SparringEngine
from azia.azia_core.intelligence.preflight_engine import PreFlightEngine

# Initialize FastMCP Server
mcp = FastMCP("AZIA-Autonomous-Design-MCP")

# Global pipeline instance and generation session registry
pipeline = AutonomousDesignPipeline()
sparring_engine = SparringEngine()
preflight_engine = PreFlightEngine()

ACTIVE_SESSIONS: Dict[str, Any] = {}
LAST_SPEC: Optional[Any] = None


@mcp.tool()
def design_product(
    requirement: str,
    platform: str = "auto",
    fidelity: str = "high",
    style: str = "auto",
    existing_figma_context: bool = True,
    autonomous: bool = True
) -> str:
    """
    MASTER CAPABILITY: Autonomously design a complete, editable, connected Figma product from a natural-language requirement.
    Executes UX architecture, information architecture, flows, design tokens, components, screens, prototypes, and QA.
    """
    global LAST_SPEC
    spec, ops, canvas, summary = pipeline.design_product(
        requirement=requirement,
        platform=platform,
        style=style,
        fidelity=fidelity,
        existing_figma_context=existing_figma_context
    )

    gen_id = summary["generation_id"]
    ACTIVE_SESSIONS[gen_id] = {
        "spec": spec,
        "ops": ops,
        "canvas": canvas,
        "summary": summary
    }
    LAST_SPEC = spec

    # Structured MCP Response format matching Section 28 of prompt
    response = {
        "status": "SUCCESS",
        "product": {
            "name": spec.metadata.product_name,
            "category": spec.metadata.product_category,
            "platform": spec.metadata.platform,
            "purpose": spec.ux_architecture.product_purpose
        },
        "generation_id": gen_id,
        "screens_created": [s.screen_name for s in spec.screens],
        "components_created": list(spec.component_registry.components.keys()),
        "flows_created": [f.title for f in spec.user_flows],
        "assumptions": [
            {"id": a.id, "statement": a.statement, "confidence": a.confidence.value}
            for a in spec.epistemic_register.explicit_assumptions
        ],
        "qa_score": summary["qa_score"],
        "issues_fixed": spec.qa_report.issues_resolved if spec.qa_report else [],
        "remaining_issues": spec.qa_report.unresolved_issues if spec.qa_report else [],
        "figma_context": {
            "operations_count": len(ops),
            "managed_by": spec.metadata.managed_by,
            "plugin_sync_ready": True
        }
    }
    return json.dumps(response, indent=2)


@mcp.tool()
def preflight_check(requirement: str) -> str:
    """
    Evaluates whether the requirement context is sufficiently specified before design generation.
    Returns completeness score and targeted clarification questions if ambiguous.
    """
    eval_res = preflight_engine.evaluate(requirement)
    return json.dumps(eval_res.model_dump(), indent=2)


@mcp.tool()
def spar_with_agent(query: str, generation_id: Optional[str] = None) -> str:
    """
    Socratic sparring partner (AZIA Balanced Critic).
    Challenge assumptions, request flow simplifications, and evaluate UX trade-offs.
    """
    global LAST_SPEC
    spec = LAST_SPEC
    if generation_id and generation_id in ACTIVE_SESSIONS:
        spec = ACTIVE_SESSIONS[generation_id]["spec"]

    if not spec:
        # Fallback run default if no prior spec
        spec, _, _, _ = pipeline.design_product("Build modern product")

    res = sparring_engine.spar(query, spec)
    return json.dumps(res.to_dict(), indent=2)


@mcp.tool()
def run_design_qa(generation_id: Optional[str] = None) -> str:
    """
    Runs dual-track QA: Visual layout adherence (8pt grid, contrast) and UX requirement coverage.
    """
    global LAST_SPEC
    spec = LAST_SPEC
    if generation_id and generation_id in ACTIVE_SESSIONS:
        spec = ACTIVE_SESSIONS[generation_id]["spec"]

    if not spec:
        return json.dumps({"error": "No active design specification found to audit."})

    report = spec.qa_report
    return json.dumps(report.model_dump() if report else {}, indent=2)


@mcp.tool()
def rollback_generation(generation_id: str) -> str:
    """
    Safely rolls back all generated content for a specific generation run without affecting user's existing work.
    """
    if generation_id in ACTIVE_SESSIONS:
        session = ACTIVE_SESSIONS[generation_id]
        deleted_count = session["canvas"].rollback_generation(generation_id)
        return json.dumps({
            "status": "SUCCESS",
            "message": f"Successfully rolled back generation {generation_id}.",
            "nodes_deleted": deleted_count
        })
    return json.dumps({
        "status": "NOT_FOUND",
        "message": f"Generation session {generation_id} not active in memory."
    })


@mcp.tool()
def get_generation_status(generation_id: str) -> str:
    """Retrieves status and summary of an active design generation."""
    if generation_id in ACTIVE_SESSIONS:
        return json.dumps(ACTIVE_SESSIONS[generation_id]["summary"], indent=2)
    return json.dumps({"status": "NOT_FOUND"})


if __name__ == "__main__":
    mcp.run()
