"""
Unit tests for AZIA Unified LLM Client (Google Gemini, xAI Grok, and Offline Fallback).
"""

import pytest
from azia.azia_core.intelligence.llm_client import LLMClient, LLMProvider
from azia.azia_core.intelligence.mentor_sparring import SparringEngine
from azia.api_server import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_llm_client_initialization_offline():
    """Verify that without API keys, client defaults safely to offline mode."""
    llm = LLMClient(gemini_api_key="", grok_api_key="")
    status = llm.get_provider_status()

    assert status["gemini"]["available"] is False
    assert status["grok"]["available"] is False
    assert status["active_provider"] == "offline"
    assert status["offline_fallback_ready"] is True

    # Generate returns None and 'offline'
    text, provider = llm.generate("Test prompt")
    assert text is None
    assert provider == "offline"


def test_llm_client_gemini_detection():
    """Verify that when Gemini key is passed, active provider becomes gemini."""
    llm = LLMClient(gemini_api_key="AIzaSyDummyKeyForTestingOnly", grok_api_key="")
    status = llm.get_provider_status()

    assert status["gemini"]["available"] is True
    assert status["active_provider"] == "gemini"


def test_llm_client_grok_detection():
    """Verify that when Grok key is passed, active provider becomes grok."""
    llm = LLMClient(gemini_api_key="", grok_api_key="xai-dummy-key-for-testing")
    status = llm.get_provider_status()

    assert status["grok"]["available"] is True
    assert status["active_provider"] == "grok"


def test_sparring_with_llm_client():
    """Verify that SparringEngine works seamlessly with LLMClient in offline/fallback mode."""
    llm = LLMClient(gemini_api_key="", grok_api_key="")
    engine = SparringEngine(llm_client=llm)

    res = engine.spar("Can we simplify this flow to 2 screens?", None)
    assert res.critique is not None
    assert len(res.trade_offs) > 0
    assert res.ai_provider == "offline"


def test_api_ai_status_and_configure():
    """Verify the /api/ai/status and /api/ai/configure REST endpoints."""
    # Check status
    resp = client.get("/api/ai/status")
    assert resp.status_code == 200
    data = resp.json()
    assert "gemini" in data
    assert "grok" in data
    assert "active_provider" in data

    # Configure dynamic key
    conf_resp = client.post("/api/ai/configure", json={"gemini_api_key": "AIzaSyTest12345"})
    assert conf_resp.status_code == 200
    assert conf_resp.json()["status"] == "SUCCESS"
    assert conf_resp.json()["active_configuration"]["gemini"]["available"] is True
