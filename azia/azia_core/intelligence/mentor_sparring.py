"""
AZIA Socratic Mentor & Sparring Partner Engine
Channels the core AZIA personality: Balanced Critic, Adaptive Mentor, with Subtle Wit and Deep UX Rigor.
Allows the designer to converse, challenge assumptions, simplify flows, and explore trade-offs.
"""

from typing import Dict, Any, List, Optional
from azia.azia_core.models.taxonomy import ConfidenceLevel, EpistemicStatus
from azia.azia_core.models.specification import ProductDesignSpecification


class SparringResponse:
    def __init__(
        self,
        critique: str,
        counterpoint: str,
        trade_offs: List[str],
        alternative_recommendation: str,
        proposed_operation_delta: Optional[Dict[str, Any]] = None,
        subtle_humor_note: Optional[str] = None
    ):
        self.critique = critique
        self.counterpoint = counterpoint
        self.trade_offs = trade_offs
        self.alternative_recommendation = alternative_recommendation
        self.proposed_operation_delta = proposed_operation_delta
        self.subtle_humor_note = subtle_humor_note

    def to_dict(self) -> Dict[str, Any]:
        return {
            "critique": self.critique,
            "counterpoint": self.counterpoint,
            "trade_offs": self.trade_offs,
            "alternative_recommendation": self.alternative_recommendation,
            "proposed_operation_delta": self.proposed_operation_delta,
            "subtle_humor_note": self.subtle_humor_note
        }


class SparringEngine:
    """Handles Socratic design sparring, assumption challenging, and flow simplification."""

    def spar(
        self,
        user_query: str,
        spec: ProductDesignSpecification
    ) -> SparringResponse:
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
