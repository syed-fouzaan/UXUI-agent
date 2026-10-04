"""
AZIA Pre-Flight Intelligence Engine
Analyzes incoming user requirements and context for ambiguity and missing critical dimensions.
Prevents ungrounded hallucinations while asking targeted, high-value questions.
"""

from typing import List, Dict, Any, Optional
from azia.azia_core.models.preflight import ClarificationQuestion, PreFlightEvaluation


class PreFlightEngine:
    """Pre-flight check evaluates whether requirement context is sufficient to safely generate a UX solution."""

    CRITICAL_DIMENSIONS = [
        ("target_user", "Who is the primary user experiencing this product?"),
        ("primary_goal", "What core problem or goal must the user accomplish?"),
        ("platform", "What is the intended device form-factor (mobile app, desktop SaaS, responsive web)?"),
        ("core_workflow", "What are the essential steps of the primary workflow?"),
    ]

    def evaluate(self, requirement: str, extra_context: Optional[str] = None) -> PreFlightEvaluation:
        text = (requirement + " " + (extra_context or "")).lower()

        missing_dimensions = []
        questions = []
        score = 1.0

        # Check target user
        user_keywords = ["user", "student", "engineer", "manager", "customer", "team", "client", "shopper", "doctor", "patient", "developer", "designer"]
        has_user = any(k in text for k in user_keywords)
        if not has_user:
            missing_dimensions.append("target_user")
            questions.append(ClarificationQuestion(
                id="Q-USER",
                dimension="target_user",
                question="Who is the primary target persona (e.g. students, enterprise admins, consumers)?",
                rationale="Persona dictates interaction density, terminology, and visual hierarchy.",
                suggested_answers=["College students on mobile", "Engineering teams on desktop", "General consumers"],
                is_blocking=False
            ))
            score -= 0.25

        # Check primary goal / core tasks
        goal_keywords = ["discover", "search", "order", "track", "manage", "assign", "pay", "create", "build", "monitor", "book", "deliver", "collaborate"]
        matched_goals = [k for k in goal_keywords if k in text]
        if len(matched_goals) < 2:
            missing_dimensions.append("core_workflow")
            questions.append(ClarificationQuestion(
                id="Q-GOAL",
                dimension="core_workflow",
                question="What specific tasks should the user be able to perform?",
                rationale="User flows and screen inventories cannot be derived without key task verbs.",
                suggested_answers=["Search, select, checkout, and live track", "Create projects, assign tasks, track kanban status"],
                is_blocking=False
            ))
            score -= 0.35

        # Check platform specification
        platform_keywords = ["mobile", "app", "ios", "android", "web", "saas", "desktop", "dashboard", "tablet"]
        has_platform = any(k in text for k in platform_keywords)
        if not has_platform:
            missing_dimensions.append("platform")
            questions.append(ClarificationQuestion(
                id="Q-PLATFORM",
                dimension="platform",
                question="What is the primary surface or platform format?",
                rationale="Layout grids, navigation patterns, and component sizes depend directly on the form factor.",
                suggested_answers=["Mobile iOS/Android (393x852)", "Web Desktop (1280x900)"],
                is_blocking=False
            ))
            score -= 0.15

        score = max(0.2, score)
        is_sufficient = score >= 0.5 or len(requirement.split()) >= 15

        # Identify inferred intent
        intent = "General application design"
        if "food" in text or "delivery" in text or "restaurant" in text:
            intent = "On-demand food discovery, ordering, and delivery experience"
        elif "project" in text or "task" in text or "saas" in text or "team" in text:
            intent = "Collaborative team project and task management workspace"

        summary = (
            f"Context sufficiency score: {int(score * 100)}%. "
            + ("Sufficient context to proceed with autonomous synthesis." if is_sufficient 
               else "Context is sparse; sensible UX defaults and documented assumptions will bridge gaps.")
        )

        return PreFlightEvaluation(
            is_sufficient=is_sufficient,
            context_score=round(score, 2),
            summary=summary,
            identified_intent=intent,
            missing_critical_dimensions=missing_dimensions,
            clarification_questions=questions,
            can_proceed_with_assumptions=True
        )
