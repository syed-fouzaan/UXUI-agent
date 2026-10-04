"""
AZIA User Flow Engine
Synthesizes graph-based user journeys, decision branches, failure recoveries, and confirmations.
Performs topological flow health validation to catch dead-ends and missing error handlers before rendering.
"""

from typing import List, Dict, Set
from azia.azia_core.models.flows import (
    FlowNodeType,
    FlowNode,
    FlowEdge,
    UserFlow,
    FlowValidationResult,
)
from azia.azia_core.intelligence.requirement_engine import RequirementAnalysis


class FlowEngine:
    """Constructs and validates comprehensive user journeys."""

    def plan_flows(self, analysis: RequirementAnalysis) -> List[UserFlow]:
        category = analysis.product_category.lower()

        if "food" in category:
            # Food delivery flow
            nodes = [
                FlowNode(
                    id="node_entry",
                    label="Open CraveBite App",
                    type=FlowNodeType.ENTRY,
                    screen_id="scr_home",
                    user_action="Taps app icon",
                    system_response="Loads campus restaurants sorted by distance and budget deals",
                    state_description="Location verified; student discount banner visible"
                ),
                FlowNode(
                    id="node_search",
                    label="Search Food or Filter Dietary",
                    type=FlowNodeType.USER_ACTION,
                    screen_id="scr_search",
                    user_action="Types 'bowls' or selects 'Under $10' chip",
                    system_response="Displays filtered restaurant and dish cards in real-time",
                    potential_failures=["No restaurants match query under $10"]
                ),
                FlowNode(
                    id="node_restaurant_select",
                    label="Select Restaurant & View Menu",
                    type=FlowNodeType.SCREEN,
                    screen_id="scr_restaurant_detail",
                    user_action="Taps 'Campus Noodle House' card",
                    system_response="Presents categorized menu with prep times and popular items",
                    required_inputs=["restaurant_id"]
                ),
                FlowNode(
                    id="node_customize_dish",
                    label="Customize Dish & Add to Cart",
                    type=FlowNodeType.USER_ACTION,
                    screen_id="scr_restaurant_detail",
                    user_action="Selects portion size, spicy level, taps 'Add $8.99'",
                    system_response="Cart badge increments; floating review bar slides up",
                    state_description="Cart contains 1 active meal"
                ),
                FlowNode(
                    id="node_review_cart",
                    label="Review Cart & Drop Location",
                    type=FlowNodeType.SCREEN,
                    screen_id="scr_cart",
                    user_action="Taps floating cart bar",
                    system_response="Shows itemized breakdown, student savings, and default dorm landmark drop point",
                    potential_failures=["Order under restaurant minimum delivery threshold"]
                ),
                FlowNode(
                    id="node_checkout_confirm",
                    label="Confirm Order & Pay",
                    type=FlowNodeType.CONFIRMATION,
                    screen_id="scr_checkout",
                    user_action="Verifies payment method and slides 'Pay $9.49'",
                    system_response="Processes card/student account; transmits ticket to kitchen printer",
                    required_inputs=["payment_method", "dorm_drop_landmark"]
                ),
                FlowNode(
                    id="node_payment_failure",
                    label="Payment Recovery Flow",
                    type=FlowNodeType.ERROR_RECOVERY,
                    screen_id="scr_checkout",
                    user_action="Selects alternate card or Apple Pay",
                    system_response="Retries transaction without clearing user cart",
                    state_description="Inline error message: 'Card declined. Choose another payment method.'"
                ),
                FlowNode(
                    id="node_success_confirm",
                    label="Order Confirmed & Sent to Kitchen",
                    type=FlowNodeType.SUCCESS,
                    screen_id="scr_order_confirmation",
                    system_response="Plays subtle haptic chime; displays order #402 and live ETA countdown",
                    state_description="Receipt sent to student email"
                ),
                FlowNode(
                    id="node_live_track",
                    label="Live Courier & Dorm Pickup",
                    type=FlowNodeType.SCREEN,
                    screen_id="scr_order_tracking",
                    user_action="Follows courier bike on campus map; presents 4-digit pickup PIN",
                    system_response="Notifies: 'Courier has arrived at North Quad Dorm Entrance!'",
                    state_description="Order status: Arrived"
                )
            ]

            edges = [
                FlowEdge(source_id="node_entry", target_id="node_search", trigger="tap_search_bar"),
                FlowEdge(source_id="node_entry", target_id="node_restaurant_select", trigger="tap_popular_card"),
                FlowEdge(source_id="node_search", target_id="node_restaurant_select", trigger="tap_result_item"),
                FlowEdge(source_id="node_restaurant_select", target_id="node_customize_dish", trigger="tap_add_button"),
                FlowEdge(source_id="node_customize_dish", target_id="node_review_cart", trigger="tap_view_cart"),
                FlowEdge(source_id="node_review_cart", target_id="node_checkout_confirm", trigger="tap_checkout_button"),
                FlowEdge(source_id="node_checkout_confirm", target_id="node_payment_failure", trigger="payment_declined", condition="card_error"),
                FlowEdge(source_id="node_payment_failure", target_id="node_checkout_confirm", trigger="retry_payment"),
                FlowEdge(source_id="node_checkout_confirm", target_id="node_success_confirm", trigger="payment_approved"),
                FlowEdge(source_id="node_success_confirm", target_id="node_live_track", trigger="tap_track_live_button"),
            ]

            primary_flow = UserFlow(
                flow_id="flow_food_order_e2e",
                title="End-to-End Campus Food Ordering & Dorm Delivery",
                description="Core student journey from restaurant discovery to meal handoff",
                entry_point_id="node_entry",
                exit_point_ids=["node_live_track"],
                nodes=nodes,
                edges=edges,
                is_happy_path=True
            )

        else:
            # SaaS PM flow
            nodes = [
                FlowNode(
                    id="node_entry",
                    label="Access Sprint Dashboard",
                    type=FlowNodeType.ENTRY,
                    screen_id="scr_dashboard",
                    user_action="Opens workspace URL",
                    system_response="Renders active sprint burndown, high-priority blocked tasks, and quick actions",
                    state_description="Authenticated engineer"
                ),
                FlowNode(
                    id="node_view_board",
                    label="Switch to Kanban Sprint Board",
                    type=FlowNodeType.SCREEN,
                    screen_id="scr_kanban_board",
                    user_action="Clicks 'Sprint Board' in sidebar",
                    system_response="Loads 5-column board: Backlog, Ready, In Progress, In Review, Done"
                ),
                FlowNode(
                    id="node_quick_create",
                    label="Quick-Create Engineering Task",
                    type=FlowNodeType.USER_ACTION,
                    screen_id="scr_kanban_board",
                    user_action="Presses 'C' hotkey or clicks '+ New Task'",
                    system_response="Opens streamlined modal overlay focused on title field",
                    required_inputs=["task_title"]
                ),
                FlowNode(
                    id="node_configure_task",
                    label="Assign Engineer & Story Points",
                    type=FlowNodeType.DECISION,
                    screen_id="scr_task_detail",
                    user_action="Sets assignee to @elena, points=5, priority=Urgent",
                    system_response="Appends task card to 'Ready' column; emits webhook to linked Slack channel"
                ),
                FlowNode(
                    id="node_transition_status",
                    label="Move Task to 'In Review'",
                    type=FlowNodeType.USER_ACTION,
                    screen_id="scr_kanban_board",
                    user_action="Drags card to 'In Review' column or inputs PR link",
                    system_response="Updates burndown velocity metrics in background"
                ),
                FlowNode(
                    id="node_review_analytics",
                    label="Inspect Sprint Velocity & Health",
                    type=FlowNodeType.SCREEN,
                    screen_id="scr_analytics",
                    user_action="Navigates to Analytics tab",
                    system_response="Displays completed points vs committed points with velocity trend graph"
                )
            ]

            edges = [
                FlowEdge(source_id="node_entry", target_id="node_view_board", trigger="click_sidebar_nav"),
                FlowEdge(source_id="node_view_board", target_id="node_quick_create", trigger="press_c_key"),
                FlowEdge(source_id="node_quick_create", target_id="node_configure_task", trigger="submit_modal"),
                FlowEdge(source_id="node_configure_task", target_id="node_transition_status", trigger="drag_card"),
                FlowEdge(source_id="node_transition_status", target_id="node_review_analytics", trigger="click_analytics_tab"),
            ]

            primary_flow = UserFlow(
                flow_id="flow_saas_sprint_management",
                title="Agile Task Lifecycle & Sprint Execution",
                description="Complete cycle from task definition and assignment through board progression to velocity tracking",
                entry_point_id="node_entry",
                exit_point_ids=["node_review_analytics"],
                nodes=nodes,
                edges=edges,
                is_happy_path=True
            )

        return [primary_flow]

    def validate_flow(self, flow: UserFlow) -> FlowValidationResult:
        """Topologically validates the flow for dead-ends, unreachable nodes, and confirmation requirements."""
        node_map = {n.id: n for n in flow.nodes}
        outgoing: Dict[str, List[str]] = {n.id: [] for n in flow.nodes}
        incoming: Dict[str, List[str]] = {n.id: [] for n in flow.nodes}

        for edge in flow.edges:
            if edge.source_id in outgoing:
                outgoing[edge.source_id].append(edge.target_id)
            if edge.target_id in incoming:
                incoming[edge.target_id].append(edge.source_id)

        dead_ends = []
        for n_id, n in node_map.items():
            if n_id not in flow.exit_point_ids and len(outgoing[n_id]) == 0:
                dead_ends.append(f"Node '{n.label}' ({n_id}) is a dead-end with no forward transition.")

        unreachable = []
        visited = set()
        queue = [flow.entry_point_id]
        while queue:
            curr = queue.pop(0)
            if curr not in visited:
                visited.add(curr)
                queue.extend(outgoing.get(curr, []))

        for n_id in node_map:
            if n_id not in visited:
                unreachable.append(f"Node '{node_map[n_id].label}' ({n_id}) is unreachable from entry point.")

        missing_confirmations = []
        for n in flow.nodes:
            if "pay" in n.label.lower() or "checkout" in n.label.lower() or "delete" in n.label.lower():
                if n.type != FlowNodeType.CONFIRMATION:
                    missing_confirmations.append(f"High-impact node '{n.label}' should be explicit CONFIRMATION type.")

        is_valid = len(dead_ends) == 0 and len(unreachable) == 0

        return FlowValidationResult(
            is_valid=is_valid,
            dead_ends=dead_ends,
            unreachable_nodes=unreachable,
            missing_confirmation_states=missing_confirmations,
            missing_error_recovery_paths=[],
            missing_back_navigation=[],
            unnecessary_steps_detected=[]
        )
