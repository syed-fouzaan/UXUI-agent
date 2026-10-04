"""
AZIA Cloud API Server (FastAPI)
Provides global REST API endpoints for web clients, Netlify frontends, and remote Figma plugins.
Can be deployed to Render, Railway, Fly.io, Google Cloud Run, or AWS with zero configuration.
"""

import sys
import os
from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Ensure azia package is accessible
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from azia.azia_core.orchestrator import AutonomousDesignPipeline
from azia.azia_core.intelligence.mentor_sparring import SparringEngine
from azia.azia_core.intelligence.simulation_engine import SimulationEngine
from azia.azia_core.intelligence.code_generator import CodeGenerator
from azia.azia_core.intelligence.design_system_ingest import DesignSystemIngestEngine
from azia.azia_core.renderer.figma_exporter import FigmaExporter

app = FastAPI(
    title="AZIA • Autonomous AI UX/UI Design API",
    description="Global REST API for Autonomous Product Design, Nielsen Audits, Socratic Sparring, Synthetic User Simulation, Code Handoff & Design System Ingestion",
    version="1.1.0"
)

# Enable CORS for Netlify, Figma plugins, and localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline = AutonomousDesignPipeline()
sparring_engine = SparringEngine()
figma_exporter = FigmaExporter()
sim_engine = SimulationEngine()
code_generator = CodeGenerator()
ds_ingest_engine = DesignSystemIngestEngine()

LAST_SPEC = None


class DesignRequest(BaseModel):
    requirement: str
    platform: Optional[str] = "auto"
    style: Optional[str] = "auto"
    fidelity: Optional[str] = "high"


class SparRequest(BaseModel):
    query: str
    context: Optional[str] = None


class SimulationRequest(BaseModel):
    requirement: Optional[str] = None
    cohort_size: Optional[int] = 50


class CodeHandoffRequest(BaseModel):
    requirement: Optional[str] = None
    framework: Optional[str] = "all"  # "react", "swiftui", "tokens", "all"


class IngestDSRequest(BaseModel):
    input_type: str  # "figma_tokens", "css", "tailwind"
    data: Any


@app.get("/")
def root():
    return {
        "service": "AZIA Autonomous Design Engine",
        "status": "ONLINE",
        "version": "1.0.0",
        "endpoints": ["/api/design", "/api/spar", "/health"]
    }


@app.get("/health")
def health():
    return {"status": "ok", "engine": "ready"}


@app.post("/api/design")
def create_design(req: DesignRequest):
    """Generates complete product design specification and deterministic Figma operations."""
    try:
        spec, ops, canvas, summary = pipeline.design_product(
            requirement=req.requirement,
            platform=req.platform,
            style=req.style,
            fidelity=req.fidelity
        )

        global LAST_SPEC
        LAST_SPEC = spec

        ops_payload = figma_exporter.export_plugin_payload(spec, ops)

        return {
            "summary": summary,
            "specification": spec.model_dump(),
            "figma_payload": ops_payload
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/spar")
def spar(req: SparRequest):
    """Converses with AZIA Socratic mentor / balanced critic."""
    try:
        global LAST_SPEC
        spec = LAST_SPEC
        if not spec:
            spec, _, _, _ = pipeline.design_product("Build modern product")
            LAST_SPEC = spec
        res = sparring_engine.spar(req.query, spec)
        return res.to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/simulation")
def run_simulation(req: SimulationRequest):
    """Simulates autonomous synthetic user cohorts across screens and predicts drop-off points."""
    try:
        global LAST_SPEC
        spec = LAST_SPEC
        if req.requirement:
            spec, _, _, _ = pipeline.design_product(req.requirement)
            LAST_SPEC = spec
        elif not spec:
            spec, _, _, _ = pipeline.design_product("Build modern food delivery application")
            LAST_SPEC = spec

        report = sim_engine.run_simulation(spec)
        spec.simulation_report = report
        return report.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/code-handoff")
def code_handoff(req: CodeHandoffRequest):
    """1-Click production-ready code handoff for React + Tailwind, SwiftUI, or W3C DTCG Tokens."""
    try:
        global LAST_SPEC
        spec = LAST_SPEC
        if req.requirement:
            spec, _, _, _ = pipeline.design_product(req.requirement)
            LAST_SPEC = spec
        elif not spec:
            spec, _, _, _ = pipeline.design_product("Build modern food delivery application")
            LAST_SPEC = spec

        fw = (req.framework or "all").lower()
        if fw == "react":
            return code_generator.generate_react_tailwind(spec).model_dump()
        elif fw == "swiftui":
            return code_generator.generate_swiftui(spec).model_dump()
        elif fw == "tokens":
            return code_generator.generate_w3c_tokens(spec).model_dump()
        else:
            return {
                "react": code_generator.generate_react_tailwind(spec).model_dump(),
                "swiftui": code_generator.generate_swiftui(spec).model_dump(),
                "tokens": code_generator.generate_w3c_tokens(spec).model_dump()
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/design-system/ingest")
def ingest_design_system(req: IngestDSRequest):
    """Ingests external Figma Tokens Studio JSON, CSS variables, or Tailwind config."""
    try:
        in_type = req.input_type.lower()
        if in_type == "figma_tokens":
            res = ds_ingest_engine.ingest_figma_tokens_studio(req.data)
        elif in_type == "css":
            res = ds_ingest_engine.ingest_css_variables(str(req.data))
        elif in_type == "tailwind":
            res = ds_ingest_engine.ingest_tailwind_theme(req.data)
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported input_type: {req.input_type}")
        return res.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("azia.api_server:app", host="0.0.0.0", port=8000, reload=True)

