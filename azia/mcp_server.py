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
from azia.azia_core.intelligence.simulation_engine import SimulationEngine
from azia.azia_core.intelligence.code_generator import CodeGenerator
from azia.azia_core.intelligence.design_system_ingest import DesignSystemIngestEngine
from azia.azia_core.intelligence.llm_client import LLMClient

# Initialize FastMCP Server
mcp = FastMCP("AZIA-Autonomous-Design-MCP")

# Global pipeline instance, LLM client, and generation session registry
llm_client = LLMClient()
pipeline = AutonomousDesignPipeline()
sparring_engine = SparringEngine(llm_client=llm_client)
preflight_engine = PreFlightEngine()
sim_engine = SimulationEngine()
code_generator = CodeGenerator()
ds_ingest_engine = DesignSystemIngestEngine()

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
def run_usability_simulation(generation_id: Optional[str] = None) -> str:
    """
    Simulates autonomous synthetic user cohorts across screens and predicts drop-off points.
    Computes visual saliency heatmaps (Itti-Koch fixation algorithm), attention hot spots,
    and cognitive friction scores.
    """
    global LAST_SPEC
    spec = LAST_SPEC
    if generation_id and generation_id in ACTIVE_SESSIONS:
        spec = ACTIVE_SESSIONS[generation_id]["spec"]

    if not spec:
        return json.dumps({"error": "No active design specification found. Run design_product first."})

    report = sim_engine.run_simulation(spec)
    spec.simulation_report = report
    return report.model_dump_json(indent=2)


@mcp.tool()
def export_production_code(generation_id: Optional[str] = None, framework: str = "react") -> str:
    """
    1-Click production-ready code handoff.
    Generates clean React 19 + Tailwind CSS, SwiftUI, or W3C DTCG Design Tokens from the active design spec.
    Supported frameworks: 'react', 'swiftui', 'tokens', 'all'.
    """
    global LAST_SPEC
    spec = LAST_SPEC
    if generation_id and generation_id in ACTIVE_SESSIONS:
        spec = ACTIVE_SESSIONS[generation_id]["spec"]

    if not spec:
        return json.dumps({"error": "No active design specification found. Run design_product first."})

    framework_lower = framework.lower()
    if framework_lower == "swiftui":
        bundle = code_generator.generate_swiftui(spec)
        return bundle.model_dump_json(indent=2)
    elif framework_lower == "tokens":
        tokens = code_generator.generate_w3c_tokens(spec)
        return tokens.model_dump_json(indent=2)
    elif framework_lower == "all":
        react_b = code_generator.generate_react_tailwind(spec)
        swift_b = code_generator.generate_swiftui(spec)
        tok_b = code_generator.generate_w3c_tokens(spec)
        return json.dumps({
            "react_tailwind": react_b.model_dump(),
            "swiftui": swift_b.model_dump(),
            "tokens": tok_b.model_dump()
        }, indent=2)
    else:
        bundle = code_generator.generate_react_tailwind(spec)
        return bundle.model_dump_json(indent=2)


@mcp.tool()
def ingest_design_system(input_type: str, data: str) -> str:
    """
    Ingests an existing design system into AZIA.
    Supported input_type: 'figma_tokens' (Tokens Studio JSON export), 'css' (CSS root variables), 'tailwind' (Tailwind config object).
    Extracted tokens are normalized to W3C standards and can be used for new product generations.
    """
    try:
        if input_type.lower() == "figma_tokens":
            parsed_data = json.loads(data) if isinstance(data, str) else data
            res = ds_ingest_engine.ingest_figma_tokens_studio(parsed_data)
        elif input_type.lower() == "css":
            res = ds_ingest_engine.ingest_css_variables(data)
        elif input_type.lower() == "tailwind":
            parsed_data = json.loads(data) if isinstance(data, str) else data
            res = ds_ingest_engine.ingest_tailwind_theme(parsed_data)
        else:
            return json.dumps({"error": f"Unsupported input_type: {input_type}. Use 'figma_tokens', 'css', or 'tailwind'."})

        return res.model_dump_json(indent=2)
    except Exception as e:
        return json.dumps({"error": f"Failed to ingest design system: {str(e)}"})


@mcp.tool()
def get_ai_provider_status() -> str:
    """
    Checks the status of Google Gemini and xAI Grok APIs.
    Reports whether cloud generative intelligence (Gemini/Grok) or offline deterministic heuristics is active.
    """
    return json.dumps(llm_client.get_provider_status(), indent=2)


@mcp.tool()
def get_generation_status(generation_id: str) -> str:
    """Retrieves status and summary of an active design generation."""
    if generation_id in ACTIVE_SESSIONS:
        return json.dumps(ACTIVE_SESSIONS[generation_id]["summary"], indent=2)
    return json.dumps({"status": "NOT_FOUND"})


if __name__ == "__main__":
    mcp.run()
