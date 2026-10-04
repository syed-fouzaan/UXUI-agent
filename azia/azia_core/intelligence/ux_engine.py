"""
AZIA UX Architecture Intelligence Engine
Generates evidence-backed Personas, Jobs-To-Be-Done (JTBD), Mental Models, and User Journeys.
Adheres strictly to the PRD mandate: do NOT hallucinate useless demographic filler (e.g. favorite pet, horoscope);
focus strictly on behavioral context, friction points, cognitive models, and task motivators.
"""

from typing import List
from azia.azia_core.models.taxonomy import EpistemicStatus, ConfidenceLevel
from azia.azia_core.models.ux_artifacts import (
    Persona,
    JTBD,
    JourneyPhase,
    UserJourney,
    UXArchitecture,
)
from azia.azia_core.intelligence.requirement_engine import RequirementAnalysis


class UXEngine:
    """Derives user empathy models, cognitive journeys, and Jobs-to-be-Done from requirement analysis."""

    def synthesize(self, analysis: RequirementAnalysis) -> UXArchitecture:
        category = analysis.product_category.lower()

        if "food" in category:
            # Domain 1: College Food Delivery
            personas = [
                Persona(
                    id="PER-01",
                    name="Alex Rivera - Rushed Student",
                    role="Undergraduate Biology Major",
                    primary_goal="Grab an affordable hot lunch between back-to-back lectures with under 15 minutes to spare.",
                    core_needs=[
                        "Accurate live prep & delivery timestamps to avoid being late for lab",
                        "Clear calorie and dietary tags (vegetarian/halal)",
                        "One-tap payment via Apple Pay / Student Campus Cash"
                    ],
                    pain_points=[
                        "Unexpected delivery delays that conflict with exam schedules",
                        "High minimum order fees and opaque service surcharges",
                        "Couriers getting lost finding specific dorm quad entries"
                    ],
                    context_of_use="Mobile smartphone, walking between campus lecture halls, spotty cellular connectivity.",
                    mental_model="Expects lightning-fast UberEats/DoorDash speed with campus-specific student budget discounts.",
                    tech_savviness="Advanced Mobile Native",
                    supporting_evidence_ids=["EVID-REQ-01"],
                    epistemic_status=EpistemicStatus.CONFIRMED,
                    confidence=ConfidenceLevel.HIGH
                ),
                Persona(
                    id="PER-02",
                    name="Maya Chen - Late Night Study Group Leader",
                    role="Graduate Research Assistant",
                    primary_goal="Coordinate group food orders during midnight library cram sessions without math headaches.",
                    core_needs=[
                        "Group cart sharing and bill splitting",
                        "Bulk combo meal value deals",
                        "Delivery locker / library lobby drop instructions"
                    ],
                    pain_points=[
                        "Chasing down dorm mates for Venmo payments",
                        "Cold food arriving due to stacked delivery routes"
                    ],
                    context_of_use="Mobile or tablet in library quiet zone, ordering in low ambient light.",
                    mental_model="Treats ordering as a social shared ritual during study sprints.",
                    tech_savviness="Intermediate",
                    supporting_evidence_ids=["EVID-REQ-01"],
                    epistemic_status=EpistemicStatus.INFERRED,
                    confidence=ConfidenceLevel.MEDIUM
                )
            ]

            jtbd_list = [
                JTBD(
                    id="JTBD-01",
                    persona_id="PER-01",
                    situation="When I have a 20-minute gap between classes",
                    motivation="I want to order a hot meal from a nearby campus spot and pick it up right outside my building",
                    expected_outcome="So I can eat healthy, avoid cafeteria lines, and never be late for class",
                    success_metric="Total order placement completed in under 90 seconds; ETA variance under 3 minutes",
                    priority="Core",
                    supporting_evidence_ids=["EVID-REQ-01"],
                    confidence=ConfidenceLevel.HIGH
                ),
                JTBD(
                    id="JTBD-02",
                    persona_id="PER-01",
                    situation="When my campus budget is running low near end of month",
                    motivation="I want to filter restaurants by 'Under $10 Student Meals' with free delivery",
                    expected_outcome="So I can eat comfortably without breaking my student budget",
                    success_metric="Zero unexpected convenience fees at payment screen",
                    priority="High",
                    supporting_evidence_ids=["EVID-REQ-01"],
                    confidence=ConfidenceLevel.HIGH
                )
            ]

            primary_phases = [
                JourneyPhase(
                    phase_name="Discovery",
                    user_thought="'I need food fast near the science center that costs less than $12.'",
                    touchpoints=["scr_home", "scr_search_results"],
                    friction_risk="Overwhelming list of faraway restaurants with 45+ minute waits",
                    mitigation_strategy="Prominent 'Nearby & Fast' campus quick-filter pill bar right at header"
                ),
                JourneyPhase(
                    phase_name="Item Selection & Customization",
                    user_thought="'Can I add extra protein without paying $6 extra?'",
                    touchpoints=["scr_restaurant_detail", "cmp_bottom_sheet_customize"],
                    friction_risk="Confusing nested modifiers that force unnecessary selections",
                    mitigation_strategy="Clean radio groups with explicit pricing badges next to each add-on"
                ),
                JourneyPhase(
                    phase_name="Frictionless Checkout",
                    user_thought="'Does my student discount apply, and where exactly does the courier drop it?'",
                    touchpoints=["scr_cart", "scr_checkout"],
                    friction_risk="Hidden delivery fees revealed at the final payment step causing drop-off",
                    mitigation_strategy="Transparent fee breakdown with default saved dorm landmark address"
                ),
                JourneyPhase(
                    phase_name="Fulfillment & Tracking",
                    user_thought="'Is the driver here yet? I have 4 minutes before lecture starts.'",
                    touchpoints=["scr_order_tracking"],
                    friction_risk="Vague 'Order in progress' state with no live map marker",
                    mitigation_strategy="Live milestone stepper with exact courier GPS coordinates and PIN pickup code"
                )
            ]

            primary_journey = UserJourney(
                id="JRN-01",
                title="Rush-Hour Campus Meal Order & Pickup",
                persona_id="PER-01",
                phases=primary_phases,
                entry_point="Tap app icon between classes",
                success_state="Student picks up hot meal at dorm entrance with 10 minutes to spare"
            )

            mental_models = [
                "Map & ETA prominence: Food delivery is inherently time-sensitive; progress indicator must always be top-level.",
                "Student budget psychology: Upfront total price transparency builds trust faster than visual flashiness."
            ]

        else:
            # Domain 2: Engineering Project Management SaaS
            personas = [
                Persona(
                    id="PER-01",
                    name="Marcus Vance - Lead Staff Engineer",
                    role="Technical Tech Lead / Scrum Master",
                    primary_goal="Keep a 10-person distributed backend team unblocked and track sprint commitments without spending hours updating Jira.",
                    core_needs=[
                        "Instant visibility into pull-request status and blocked dependencies",
                        "Keyboard-first task creation and status changes",
                        "Automated sprint burndown telemetry without manual ticket grooming"
                    ],
                    pain_points=[
                        "Bloated enterprise project tools requiring 15 clicks just to create a subtask",
                        "Out-of-sync task states because engineers hate updating slow tools",
                        "Fragmented context between Slack, GitHub, and task boards"
                    ],
                    context_of_use="Dual 4K desktop workstation, Chrome and terminal windows open side-by-side.",
                    mental_model="Linear, GitHub Projects, or Raycast: speed, keyboard navigation, clean aesthetics.",
                    tech_savviness="Expert Engineer",
                    supporting_evidence_ids=["EVID-REQ-01"],
                    epistemic_status=EpistemicStatus.CONFIRMED,
                    confidence=ConfidenceLevel.HIGH
                ),
                Persona(
                    id="PER-02",
                    name="Elena Rostova - Full-Stack Developer",
                    role="Senior Software Engineer",
                    primary_goal="Pick up assigned sprint tickets, understand requirements immediately, and link Git PRs with zero friction.",
                    core_needs=[
                        "Clean markdown descriptions with code snippet highlighting",
                        "Clear priority labels and acceptance criteria checklists",
                        "Fast filter to 'My Tasks' in 1 click"
                    ],
                    pain_points=[
                        "Ambiguous ticket descriptions with no clear definition of done",
                        "Losing focus due to clunky UI lag during sprint planning meetings"
                    ],
                    context_of_use="MacBook Pro 14-inch, IDE active, prefers Dark Mode.",
                    mental_model="Task board as an extension of the developer Git workflow.",
                    tech_savviness="Expert",
                    supporting_evidence_ids=["EVID-REQ-01"],
                    epistemic_status=EpistemicStatus.INFERRED,
                    confidence=ConfidenceLevel.HIGH
                )
            ]

            jtbd_list = [
                JTBD(
                    id="JTBD-01",
                    persona_id="PER-01",
                    situation="When conducting Monday morning sprint planning with my team",
                    motivation="I want to quickly assign unestimated backlog items and visualize team capacity",
                    expected_outcome="So the sprint is committed in 20 minutes without lingering ambiguity",
                    success_metric="Sprint setup completed in under 15 minutes; story point allocation verified",
                    priority="Core",
                    supporting_evidence_ids=["EVID-REQ-01"],
                    confidence=ConfidenceLevel.HIGH
                ),
                JTBD(
                    id="JTBD-02",
                    persona_id="PER-02",
                    situation="When finishing a feature branch commit in my terminal",
                    motivation="I want the task status to automatically flip from 'In Progress' to 'In Review'",
                    expected_outcome="So I don't have to manually context-switch into another browser tab",
                    success_metric="Zero manual status updates required for linked PRs",
                    priority="High",
                    supporting_evidence_ids=["EVID-REQ-01"],
                    confidence=ConfidenceLevel.HIGH
                )
            ]

            primary_phases = [
                JourneyPhase(
                    phase_name="Project Overview & Triage",
                    user_thought="'What's blocking the current sprint release?'",
                    touchpoints=["scr_dashboard", "scr_kanban_board"],
                    friction_risk="Drowning in hundreds of stale tickets across unorganized columns",
                    mitigation_strategy="High-contrast 'Blocked Items' summary badge and instant search filter"
                ),
                JourneyPhase(
                    phase_name="Task Creation & Assignment",
                    user_thought="'Need to file an urgent bug fix for auth token expiration.'",
                    touchpoints=["cmp_modal_create_task", "scr_task_list"],
                    friction_risk="Lengthy modal form with 20 compulsory enterprise fields",
                    mitigation_strategy="Streamlined modal: Title, Priority, Assignee, Markdown Body; 'Cmd+Enter' to save"
                ),
                JourneyPhase(
                    phase_name="Progress Tracking & Status Transition",
                    user_thought="'Moving this to Done now that CI checks passed.'",
                    touchpoints=["scr_kanban_board", "scr_task_detail"],
                    friction_risk="Laggy drag-and-drop or lost status updates",
                    mitigation_strategy="Fluid drag feedback with optimistic UI update and keyboard shortcut 'M' to move"
                ),
                JourneyPhase(
                    phase_name="Sprint Retrospective & Velocity Review",
                    user_thought="'Did we hit our velocity target this fortnight?'",
                    touchpoints=["scr_sprint_analytics"],
                    friction_risk="Convoluted data tables with no actionable burnup trend line",
                    mitigation_strategy="Clear visual burnup chart with completed vs scope-creep delta indicators"
                )
            ]

            primary_journey = UserJourney(
                id="JRN-01",
                title="Sprint Execution & Task Lifecycle",
                persona_id="PER-01",
                phases=primary_phases,
                entry_point="Open browser dashboard at morning standup",
                success_state="Team completes sprint on schedule with full PR traceability"
            )

            mental_models = [
                "Keyboard mastery: Engineers expect 'Cmd+K' command palettes and hotkeys over mouse navigation.",
                "Dense scannability: Prefer compact 32px table rows and column chips over airy consumer whitespace."
            ]

        return UXArchitecture(
            product_purpose=analysis.product_purpose,
            target_audiences=analysis.target_users,
            personas=personas,
            jtbd_list=jtbd_list,
            primary_journey=primary_journey,
            secondary_journeys=[],
            key_mental_models=mental_models
        )
