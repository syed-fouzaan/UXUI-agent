"""
AZIA Unified LLM Intelligence Gateway (Google Gemini & xAI Grok Free/Standard APIs)
Provides resilient, high-speed LLM generation with automatic provider fallbacks:
1. Google Gemini API (gemini-2.0-flash / gemini-1.5-flash - generous free tier)
2. xAI Grok API (grok-beta / grok-2 via xAI OpenAI-compatible API)
3. Safe Fallback to AZIA Native Deterministic Heuristic Engine
"""

import os
import json
import logging
from enum import Enum
from typing import Optional, Dict, Any, Tuple
import httpx

# Attempt to load local environment variables from .env
try:
    from dotenv import load_dotenv
    load_dotenv()
    # Also check azia/.env
    azia_env = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
    if os.path.exists(azia_env):
        load_dotenv(azia_env)
except Exception:
    pass

logger = logging.getLogger("azia.llm_client")


class LLMProvider(str, Enum):
    GEMINI = "gemini"
    GROK = "grok"
    OFFLINE_DETERMINISTIC = "offline"


class LLMClient:
    """Unified client orchestrating Google Gemini and xAI Grok APIs with offline fallback."""

    def __init__(
        self,
        gemini_api_key: Optional[str] = None,
        grok_api_key: Optional[str] = None,
        gemini_model: str = "gemini-2.0-flash",
        grok_model: str = "grok-beta",
        timeout_seconds: float = 12.0
    ):
        self.gemini_api_key = gemini_api_key or os.getenv("GEMINI_API_KEY")
        self.grok_api_key = grok_api_key or os.getenv("GROK_API_KEY") or os.getenv("XAI_API_KEY")
        self.gemini_model = gemini_model
        self.grok_model = grok_model
        self.timeout = timeout_seconds

    def get_provider_status(self) -> Dict[str, Any]:
        """Returns the readiness of configured AI providers."""
        gemini_ready = bool(self.gemini_api_key and len(self.gemini_api_key.strip()) > 5)
        grok_ready = bool(self.grok_api_key and len(self.grok_api_key.strip()) > 5)

        active = LLMProvider.OFFLINE_DETERMINISTIC
        if gemini_ready:
            active = LLMProvider.GEMINI
        elif grok_ready:
            active = LLMProvider.GROK

        return {
            "gemini": {
                "available": gemini_ready,
                "model": self.gemini_model,
                "tier": "Google AI Studio Free Tier / Standard"
            },
            "grok": {
                "available": grok_ready,
                "model": self.grok_model,
                "tier": "xAI API"
            },
            "active_provider": active.value,
            "offline_fallback_ready": True
        }

    def call_gemini(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.4,
        max_tokens: int = 1500
    ) -> Optional[str]:
        """Calls Google Gemini API (gemini-2.0-flash / gemini-1.5-flash)."""
        if not self.gemini_api_key:
            return None

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.gemini_model}:generateContent?key={self.gemini_api_key}"

        contents = []
        if system_prompt:
            contents.append({
                "role": "user",
                "parts": [{"text": f"SYSTEM INSTRUCTION: {system_prompt}"}]
            })
            contents.append({
                "role": "model",
                "parts": [{"text": "Understood. I will act strictly according to the system instructions."}]
            })

        contents.append({
            "role": "user",
            "parts": [{"text": prompt}]
        })

        payload = {
            "contents": contents,
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_tokens
            }
        }

        try:
            with httpx.Client(timeout=self.timeout) as client:
                resp = client.post(url, json=payload, headers={"Content-Type": "application/json"})
                if resp.status_code == 200:
                    data = resp.json()
                    candidates = data.get("candidates", [])
                    if candidates:
                        parts = candidates[0].get("content", {}).get("parts", [])
                        if parts:
                            return parts[0].get("text", "").strip()
                else:
                    logger.warning(f"Gemini API returned status {resp.status_code}: {resp.text[:200]}")
        except Exception as e:
            logger.warning(f"Gemini API call failed: {e}")

        return None

    def call_grok(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.4,
        max_tokens: int = 1500
    ) -> Optional[str]:
        """Calls xAI Grok API via standard OpenAI-compatible endpoint."""
        if not self.grok_api_key:
            return None

        url = "https://api.x.ai/v1/chat/completions"
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        payload = {
            "model": self.grok_model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False
        }

        headers = {
            "Authorization": f"Bearer {self.grok_api_key}",
            "Content-Type": "application/json"
        }

        try:
            with httpx.Client(timeout=self.timeout) as client:
                resp = client.post(url, json=payload, headers=headers)
                if resp.status_code == 200:
                    data = resp.json()
                    choices = data.get("choices", [])
                    if choices:
                        return choices[0].get("message", {}).get("content", "").strip()
                else:
                    logger.warning(f"Grok API returned status {resp.status_code}: {resp.text[:200]}")
        except Exception as e:
            logger.warning(f"Grok API call failed: {e}")

        return None

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        preferred_provider: Optional[str] = None,
        temperature: float = 0.4,
        max_tokens: int = 1500
    ) -> Tuple[Optional[str], str]:
        """
        Intelligently generates text with multi-provider cascade:
        1. Preferred provider (if specified and configured)
        2. Google Gemini (primary free tier)
        3. xAI Grok (secondary)
        4. Offline heuristic fallback (returns None so caller uses deterministic math)
        """
        pref = (preferred_provider or "").lower()

        # Try preferred first
        if pref == "grok" and self.grok_api_key:
            res = self.call_grok(prompt, system_prompt, temperature, max_tokens)
            if res:
                return res, LLMProvider.GROK.value

        if pref == "gemini" and self.gemini_api_key:
            res = self.call_gemini(prompt, system_prompt, temperature, max_tokens)
            if res:
                return res, LLMProvider.GEMINI.value

        # Auto-cascade: Gemini first
        if self.gemini_api_key:
            res = self.call_gemini(prompt, system_prompt, temperature, max_tokens)
            if res:
                return res, LLMProvider.GEMINI.value

        # Cascade: Grok second
        if self.grok_api_key:
            res = self.call_grok(prompt, system_prompt, temperature, max_tokens)
            if res:
                return res, LLMProvider.GROK.value

        # Offline fallback
        return None, LLMProvider.OFFLINE_DETERMINISTIC.value
