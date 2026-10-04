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
from azia.azia_core.renderer.figma_exporter import FigmaExporter

app = FastAPI(
    title="AZIA • Autonomous AI UX/UI Design API",
    description="Global REST API for Autonomous Product Design, Nielsen Audits, and Socratic Sparring",
    version="1.0.0"
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


class DesignRequest(BaseModel):
    requirement: str
    platform: Optional[str] = "auto"
    style: Optional[str] = "auto"
    fidelity: Optional[str] = "high"


class SparRequest(BaseModel):
    query: str
    context: Optional[str] = None


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
        # Run baseline spec for context
        spec, _, _, _ = pipeline.design_product("Build modern product")
        res = sparring_engine.spar(req.query, spec)
        return res.to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("azia.api_server:app", host="0.0.0.0", port=8000, reload=True)
