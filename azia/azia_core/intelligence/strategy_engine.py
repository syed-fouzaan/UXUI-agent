"""
AZIA Non-Disruptive Launch Strategy Engine
Analyzes delta between legacy user expectations and new features.
Synthesizes Progressive Disclosure ladders, Opt-In Feature Toggles, Contextual Onboarding, and Safe Fallbacks.
"""

from typing import List
from azia.azia_core.models.strategy import (
    RiskLevel,
    RolloutMechanism,
    FallbackWorkflow,
    NonDisruptiveStrategy,
)
from azia.azia_core.intelligence.requirement_engine import RequirementAnalysis


class StrategyEngine:
    """Formulates a safe, zero-disruption rollout plan for the newly designed experience."""

    def formulate_strategy(self, analysis: RequirementAnalysis) -> NonDisruptiveStrategy:
        category = analysis.product_category.lower()

        if "food" in category:
            primary_risks = [
                "Introducing new campus dorm drop points might confuse students used to curbside pickup.",
                "Student savings vouchers could fail to apply if campus identity system has downtime.",
                "Customizer bottom sheet adds cognitive friction for rushed students between classes."
            ]
            disclosure_steps = [
                "Step 1: Baseline Entry - Retain 1-tap reorder carousel at the top of Home for established users.",
                "Step 2: Contextual Teaser - Show subtle '📍 Delivered right to your dorm bike rack' pill tag on restaurant cards.",
                "Step 3: Advanced Controls - Expose group-order split and dietary allergy filter inside bottom sheet only when tapped."
            ]
            opt_in = "User can toggle 'Use Classic Curbside Delivery' in checkout delivery preferences."
            onboarding_trigger = "First time user reaches checkout with a campus address, show a 1-sentence tooltip explaining the dorm pickup landmark."
            fallbacks = [
                FallbackWorkflow(
                    failure_trigger="Campus GPS or building landmark lookup fails",
                    fallback_behavior="Default to main campus student center address with manual text field for dorm room instructions.",
                    preserves_data=True,
                    user_messaging="We couldn't pin your exact dorm. Enter your hall name or pick up at the Student Center."
                ),
                FallbackWorkflow(
                    failure_trigger="Apple Pay or Student Card service timeout",
                    fallback_behavior="Keep cart intact and immediately show alternate credit/debit card entry with 1 tap.",
                    preserves_data=True,
                    user_messaging="Campus ID balance unavailable right now. Your items are safe in cart. Pay with card?"
                )
            ]
            risk_level = RiskLevel.LOW
            impact_score = 3

        else:
            primary_risks = [
                "Changing task status interaction may disrupt established muscle-memory during standups.",
                "Automated Git PR linking might surprise engineers if tickets update without explicit confirmation.",
                "New analytics dashboard adds visual weight to the sidebar navigation."
            ]
            disclosure_steps = [
                "Step 1: Baseline Entry - Keep standard Kanban drag-and-drop identical to existing agile boards.",
                "Step 2: Contextual Teaser - When task is moved to 'In Review', prompt: 'Link branch feat/auth? [Link once] [Always auto-link]'.",
                "Step 3: Advanced Controls - Velocity burndown charts live in dedicated 'Analytics' tab rather than cluttering daily board."
            ]
            opt_in = "Settings > Workflow > 'Enable automated GitHub status transitions' (Default: Opt-in with confirmation banner)."
            onboarding_trigger = "Show non-modal toast when first commit with issue key ENG-xxx is pushed: 'We detected a linked commit! Click to view status update.'."
            fallbacks = [
                FallbackWorkflow(
                    failure_trigger="GitHub Webhook or CI status API rate-limited",
                    fallback_behavior="Allow manual drag status change with an informational indicator: 'PR status check delayed'.",
                    preserves_data=True,
                    user_messaging="Git sync is running slow. You can still move tasks manually."
                ),
                FallbackWorkflow(
                    failure_trigger="Engineer accidentally moves card to 'Done' prematurely",
                    fallback_behavior="Provide instant 'Undo' floating snackbar for 8 seconds and log undo action in task history.",
                    preserves_data=True,
                    user_messaging="Task moved to Done. [Undo (Z)]"
                )
            ]
            risk_level = RiskLevel.MEDIUM
            impact_score = 4

        return NonDisruptiveStrategy(
            existing_flow_risk=risk_level,
            primary_risks=primary_risks,
            recommended_mechanism=RolloutMechanism.PROGRESSIVE_DISCLOSURE,
            progressive_disclosure_steps=disclosure_steps,
            opt_in_toggle_spec=opt_in,
            contextual_onboarding_trigger=onboarding_trigger,
            safe_fallbacks=fallbacks,
            impact_score_1_to_10=impact_score
        )
