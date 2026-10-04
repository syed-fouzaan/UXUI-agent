"""
AZIA Socratic Mentor & Sparring Partner Engine
Channels the core AZIA personality: Balanced Critic, Adaptive Mentor, with Subtle Wit and Deep UX Rigor.
Allows the designer to converse, challenge assumptions, simplify flows, and explore trade-offs.
"""

import json
import re
from typing import Dict, Any, List, Optional
from azia.azia_core.models.taxonomy import ConfidenceLevel, EpistemicStatus
from azia.azia_core.models.specification import ProductDesignSpecification
from azia.azia_core.intelligence.llm_client import LLMClient


class SparringResponse:
    def __init__(
        self,
        critique: str,
        counterpoint: str,
        trade_offs: List[str],
        alternative_recommendation: str,
        proposed_operation_delta: Optional[Dict[str, Any]] = None,
        subtle_humor_note: Optional[str] = None,
        ai_provider: str = "offline"
    ):
        self.critique = critique
        self.counterpoint = counterpoint
        self.trade_offs = trade_offs
        self.alternative_recommendation = alternative_recommendation
        self.proposed_operation_delta = proposed_operation_delta
        self.subtle_humor_note = subtle_humor_note
        self.ai_provider = ai_provider

    def to_dict(self) -> Dict[str, Any]:
        return {
            "critique": self.critique,
            "counterpoint": self.counterpoint,
            "trade_offs": self.trade_offs,
            "alternative_recommendation": self.alternative_recommendation,
            "proposed_operation_delta": self.proposed_operation_delta,
            "subtle_humor_note": self.subtle_humor_note,
            "ai_provider": self.ai_provider
        }


class SparringEngine:
    """Handles Socratic design sparring powered by Google Gemini, xAI Grok, or native UX heuristics."""

    def __init__(self, llm_client: Optional[LLMClient] = None):
        self.llm_client = llm_client or LLMClient()

    def _spar_with_llm(self, user_query: str, spec: ProductDesignSpecification) -> Optional[SparringResponse]:
        """Calls Gemini or Grok for deep contextual Socratic sparring."""
        product_name = spec.metadata.product_name if spec else "Active Product"
        category = spec.metadata.product_category if spec else "Application"
        screens = [s.screen_name for s in spec.screens] if spec else []

        system_prompt = (
            "You are AZIA Balanced Critic, an elite autonomous UX Architect & Principal Product Designer. "
            "You evaluate design decisions with deep rigor, balancing user cognitive load, Jakob Nielsen heuristics, "
            "and business trade-offs. Provide concise, high-value architectural critiques with subtle wit. "
            "You MUST respond ONLY with a valid JSON object with the following exact keys:\n"
            "{\n"
            '  "critique": "Insightful critique of the premise",\n'
            '  "counterpoint": "Alternative perspective or defense of the pattern",\n'
            '  "trade_offs": ["Pro: ...", "Con: ..."],\n'
            '  "alternative_recommendation": "Concrete actionable alternative layout or interaction",\n'
            '  "subtle_humor_note": "A short witty sign-off with an emoji"\n'
            "}"
        )

        user_prompt = (
            f"Context: Designing '{product_name}' ({category}). Screens: {', '.join(screens)}.\n"
            f"Designer Question/Challenge: \"{user_query}\"\n"
            "Spar with the designer, challenge assumptions, and evaluate UX trade-offs. Return JSON only."
        )

        raw_text, provider = self.llm_client.generate(user_prompt, system_prompt=system_prompt)
        if not raw_text:
            return None

        try:
            # Extract JSON block if wrapped in markdown
            json_str = raw_text.strip()
            if "```" in json_str:
                m = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", json_str)
                if m:
                    json_str = m.group(1).strip()

            parsed = json.loads(json_str)
            return SparringResponse(
                critique=parsed.get("critique", raw_text),
                counterpoint=parsed.get("counterpoint", "Consider Hick's Law and user cognitive bandwidth."),
                trade_offs=parsed.get("trade_offs", ["Simplicity vs Customization"]),
                alternative_recommendation=parsed.get("alternative_recommendation", "Progressive disclosure."),
                subtle_humor_note=parsed.get("subtle_humor_note", f"Powered by {provider.title()} 💡"),
                ai_provider=provider
            )
        except Exception:
            return None

    def spar(
        self,
        user_query: str,
        spec: ProductDesignSpecification
    ) -> SparringResponse:
        # 1. Try Gemini / Grok if configured
        if self.llm_client.get_provider_status()["active_provider"] != "offline":
            llm_res = self._spar_with_llm(user_query, spec)
            if llm_res:
                return llm_res

        query_lower = user_query.lower()


        # Case 1: Flow simplification ("This flow is too long. Can we simplify it?")
        if "simplify" in query_lower or "too long" in query_lower or "too many steps" in query_lower:
            critique = (
                "I appreciate the instinct to cut steps, but let's check Hick's Law and cognitive load. "
                "Collapsing two distinct decisions (e.g. dish customization + payment authorization) into one screen "
                "increases error rates, especially when users are in a rush."
            )
            counterpoint = (
                "However, we CAN eliminate the intermediate review step if default payment and delivery landmark are pre-filled."
            )
            trade_offs = [
                "Pro: Drops time-to-order by ~35% for frequent re-orders.",
                "Con: Increases accidental orders if the student recently moved dorm buildings."
            ]
            alt = (
                "Keep the 2-step flow for first-time orders, but expose a 1-tap 'Reorder Favorite to Current Dorm' "
                "swipe affordance directly on the Home feed."
            )
            humor = "Let's find the friction before it finds your users. 🐟"

            return SparringResponse(
                critique=critique,
                counterpoint=counterpoint,
                trade_offs=trade_offs,
                alternative_recommendation=alt,
                subtle_humor_note=humor,
                proposed_operation_delta={"action": "add_express_reorder_carousel", "target_screen": "scr_home"}
            )

        # Case 2: Challenge assumption ("Challenge my assumption that users want this on the dashboard")
        elif "challenge" in query_lower or "assumption" in query_lower or "dashboard" in query_lower:
            critique = (
                "Let's interrogate that assumption. Putting this feature globally on the dashboard assumes users think in terms of global navigation. "
                "In reality, users experience this need contextually during task execution."
            )
            counterpoint = (
                "A dashboard entry point maximizes discoverability during day 1, but creates chronic visual noise on days 2 through 300."
            )
            trade_offs = [
                "Dashboard Placement: High initial awareness, but clutters primary workspace KPI scanning.",
                "Contextual Trigger: Lower initial awareness, but near-zero interaction cost when the need actually arises."
            ]
            alt = (
                "Adopt Progressive Disclosure: Keep the dashboard entry point lightweight (a compact summary widget), "
                "and embed the full capability contextually within the active workflow screen."
            )
            humor = "Remember: when everything on the dashboard is important, nothing is important."

            return SparringResponse(
                critique=critique,
                counterpoint=counterpoint,
                trade_offs=trade_offs,
                alternative_recommendation=alt,
                subtle_humor_note=humor
            )

        # Case 3: Alternative flow request ("Show me an alternative flow")
        elif "alternative" in query_lower or "different flow" in query_lower or "variant" in query_lower:
            critique = (
                "Here is an alternative architectural paradigm: instead of a linear screen-to-screen pipeline, "
                "we can structure this as an Inline Contextual Drawer (Master-Detail pattern)."
            )
            counterpoint = (
                "This preserves existing canvas context and allows users to compare details side-by-side without losing page state."
            )
            trade_offs = [
                "Full-page Flow: Better for complex multi-input workflows and mobile viewports.",
                "Side Drawer: Superior for quick edits, code review, and desktop productivity."
            ]
            alt = "Switch secondary actions to slide-over drawers while keeping primary checkout in a dedicated focused view."
            humor = "Choice architecture at its finest! 🎨"

            return SparringResponse(
                critique=critique,
                counterpoint=counterpoint,
                trade_offs=trade_offs,
                alternative_recommendation=alt,
                subtle_humor_note=humor
            )

        # Default intelligent sparring response
        else:
            critique = (
                f"I've analyzed your prompt regarding '{user_query}'. "
                "From a UX perspective, every design decision must trace back to user motivation or explicit constraints."
            )
            counterpoint = "Let's ensure we aren't designing for hypothetical edge-cases at the expense of the primary 80% happy path."
            trade_offs = [
                "Speed vs Configurability: High customization adds cognitive fatigue.",
                "Simplicity vs Power: Hiding options too deep increases interaction cost."
            ]
            alt = "Validate with 5 real users before committing to major layout refactoring."
            humor = "AZIA is on the case! 🔍"

            return SparringResponse(
                critique=critique,
                counterpoint=counterpoint,
                trade_offs=trade_offs,
                alternative_recommendation=alt,
                subtle_humor_note=humor
            )
