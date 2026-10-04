"""
AZIA Screen Planning Engine
Derives the complete set of required screens with Auto Layout structures, semantic sections,
component instances, content bindings, and state variations (default, empty, loading, error).
"""

from typing import List, Dict, Any
from azia.azia_core.models.screens import (
    ScreenLayout,
    ComponentInstanceSpec,
    ScreenSection,
    ScreenStateVariation,
    ScreenSpec,
)
from azia.azia_core.intelligence.requirement_engine import RequirementAnalysis
from azia.azia_core.intelligence.content_engine import ContentEngine


class ScreenEngine:
    """Plans full screen layouts, hierarchies, and component instances."""

    def __init__(self):
        self.content_engine = ContentEngine()

    def plan_screens(self, analysis: RequirementAnalysis) -> List[ScreenSpec]:
        category = analysis.product_category.lower()
        platform = analysis.platform.lower()
        content = self.content_engine.generate_domain_content(analysis)

        screens = []

        if "food" in category:
            # 1. Home / Discovery Feed Screen
            scr_home = ScreenSpec(
                screen_id="scr_home",
                screen_name="Campus Discovery & Feed",
                purpose="Present campus dining spots, flash student budget deals, and immediate search affordance.",
                user_goal="Find an appetizing meal nearby with minimal cognitive effort.",
                entry_conditions=["App launch", "Navigation tap on Explore"],
                exit_actions=["Tap search bar -> scr_search", "Tap restaurant card -> scr_restaurant_detail"],
                primary_cta="Explore Student Deals",
                secondary_actions=["Filter Dietary", "Change Campus Dorm Address"],
                content_hierarchy=["Header & Dorm Location", "Search Bar", "Student Saver Filters", "Nearby Flash Deals", "Popular Campus Restaurants"],
                layout=ScreenLayout(width=393, height=852, direction="vertical", padding_top=48, padding_bottom=90, padding_left=16, padding_right=16, gap=16),
                sections=[
                    ScreenSection(
                        section_id="sec_home_header",
                        title="Dorm Delivery Location & Search",
                        direction="vertical",
                        gap=12,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_loc_chip",
                                component_ref="cmp_status_badge",
                                name="Delivery Address Bar",
                                content_data={"label": "📍 North Quad Dorms (Building B)", "type": "location"}
                            ),
                            ComponentInstanceSpec(
                                instance_id="inst_search_input",
                                component_ref="cmp_search_bar",
                                name="Global Search Input",
                                content_data={"placeholder": "Search 'noodles', 'late night', 'burritos'...", "icon": "search"},
                                interactive_target_screen_id="scr_search"
                            )
                        ]
                    ),
                    ScreenSection(
                        section_id="sec_dietary_pills",
                        title="Student Saver Quick Filters",
                        direction="horizontal",
                        gap=8,
                        components=[
                            ComponentInstanceSpec(
                                instance_id=f"inst_filter_{i}",
                                component_ref="cmp_status_badge",
                                name=f"Filter Pill: {f['label']}",
                                content_data={"label": f["label"], "active": f["active"]}
                            ) for i, f in enumerate(content["quick_filters"])
                        ]
                    ),
                    ScreenSection(
                        section_id="sec_restaurant_cards",
                        title="Fast & Nearby Campus Favorites",
                        direction="vertical",
                        gap=16,
                        components=[
                            ComponentInstanceSpec(
                                instance_id=f"inst_rest_{r['id']}",
                                component_ref="cmp_entity_card",
                                name=f"Restaurant Card: {r['name']}",
                                content_data=r,
                                interactive_target_screen_id="scr_restaurant_detail"
                            ) for r in content["restaurants"]
                        ]
                    )
                ],
                states=[
                    ScreenStateVariation(
                        state_type="empty",
                        trigger_condition="No restaurants deliver after 2 AM",
                        visual_changes_description="Display Empty State: 'All kitchens closed. Pre-order for breakfast at 8 AM.'"
                    ),
                    ScreenStateVariation(
                        state_type="loading",
                        trigger_condition="Initial GPS geolocation lock",
                        visual_changes_description="Display subtle skeleton pulses for restaurant cards"
                    )
                ],
                navigation_bar_visible=True,
                prototype_destinations={"inst_search_input": "scr_search", "inst_rest_rest_01": "scr_restaurant_detail"}
            )
            screens.append(scr_home)

            # 2. Search & Filter Screen
            scr_search = ScreenSpec(
                screen_id="scr_search",
                screen_name="Dietary Search & Query Results",
                purpose="Allow granular filtering by price, prep speed, and campus building drop point.",
                user_goal="Find meals strictly matching budget ($10 or less) and dietary requirements.",
                entry_conditions=["Tap search bar on Home screen"],
                exit_actions=["Tap back -> scr_home", "Tap dish item -> scr_restaurant_detail"],
                primary_cta="Apply 2 Filters",
                secondary_actions=["Clear Search Query", "Sort by Distance"],
                content_hierarchy=["Active Search Bar", "Recent Student Queries", "Filter Chips", "Matching Dish Results"],
                layout=ScreenLayout(width=393, height=852, direction="vertical", padding_top=48, padding_bottom=90, padding_left=16, padding_right=16, gap=16),
                sections=[
                    ScreenSection(
                        section_id="sec_search_active_bar",
                        title="Query Input with Back Button",
                        direction="horizontal",
                        gap=8,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_back_btn",
                                component_ref="cmp_icon_button",
                                name="Back Arrow",
                                content_data={"icon": "chevron-left"},
                                interactive_target_screen_id="scr_home"
                            ),
                            ComponentInstanceSpec(
                                instance_id="inst_active_search_input",
                                component_ref="cmp_search_bar",
                                name="Focused Search Input",
                                content_data={"query": "chili garlic noodles", "has_clear": True}
                            )
                        ]
                    ),
                    ScreenSection(
                        section_id="sec_search_results_list",
                        title="Matched Meals Under $10",
                        direction="vertical",
                        gap=12,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_search_res_01",
                                component_ref="cmp_entity_card",
                                name="Result Card: Crispy Garlic Noodles",
                                content_data={
                                    "title": "Crispy Chili Garlic Noodles",
                                    "restaurant": "Quad Noodle Bar",
                                    "price": "$8.49",
                                    "eta": "15 min",
                                    "rating": "4.9 ⭐"
                                },
                                interactive_target_screen_id="scr_restaurant_detail"
                            )
                        ]
                    )
                ],
                prototype_destinations={"inst_back_btn": "scr_home", "inst_search_res_01": "scr_restaurant_detail"}
            )
            screens.append(scr_search)

            # 3. Restaurant Menu & Dish Detail Screen
            scr_detail = ScreenSpec(
                screen_id="scr_restaurant_detail",
                screen_name="Restaurant Menu & Customizer",
                purpose="Explore restaurant menu sections and customize toppings, spice levels, and portions.",
                user_goal="Select an item, customize it to taste, and verify total price.",
                entry_conditions=["Tap restaurant card on Home or Search"],
                exit_actions=["Tap back -> scr_home", "Tap floating cart bar -> scr_cart"],
                primary_cta="Add to Order • $8.49",
                secondary_actions=["View Dietary Allergy Info", "Share Group Cart Link"],
                content_hierarchy=["Hero Cover Image", "Restaurant Badges & ETA", "Menu Categories", "Dish Card with Add Trigger", "Floating Cart Bar"],
                layout=ScreenLayout(width=393, height=852, direction="vertical", padding_top=0, padding_bottom=90, padding_left=16, padding_right=16, gap=16),
                sections=[
                    ScreenSection(
                        section_id="sec_detail_header",
                        title="Restaurant Hero & Info",
                        direction="vertical",
                        gap=8,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_rest_hero_info",
                                component_ref="cmp_entity_card",
                                name="Restaurant Metadata Box",
                                content_data={
                                    "name": "Quad Noodle Bar & Dumplings",
                                    "rating": "4.9 (1,240 reviews)",
                                    "badge": "Student Special: Free Delivery",
                                    "hours": "Open until 1:00 AM"
                                }
                            )
                        ]
                    ),
                    ScreenSection(
                        section_id="sec_menu_items",
                        title="Popular Student Combos",
                        direction="vertical",
                        gap=12,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_dish_01",
                                component_ref="cmp_entity_card",
                                name="Dish Item: Garlic Noodles",
                                content_data={
                                    "name": "Crispy Chili Garlic Noodles",
                                    "desc": "Hand-pulled noodles with savory chili crunch, scallions & toasted peanuts",
                                    "price": "$8.49",
                                    "badge": "Bestseller 🔥"
                                }
                            )
                        ]
                    ),
                    ScreenSection(
                        section_id="sec_sticky_cart_bar",
                        title="Floating Cart Summary Bar",
                        direction="horizontal",
                        gap=12,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_btn_view_cart",
                                component_ref="cmp_btn_primary",
                                name="View Cart (2 Items) • $11.99",
                                content_data={"label": "View Cart • $11.99", "badge": "2"},
                                interactive_target_screen_id="scr_cart"
                            )
                        ]
                    )
                ],
                prototype_destinations={"inst_btn_view_cart": "scr_cart"}
            )
            screens.append(scr_detail)

            # 4. Cart & Dorm Drop Review Screen
            scr_cart = ScreenSpec(
                screen_id="scr_cart",
                screen_name="Cart & Student Discount Review",
                purpose="Review item quantities, apply promo codes, select campus landmark drop point.",
                user_goal="Verify total price with discounts applied before final payment.",
                entry_conditions=["Tap View Cart button"],
                exit_actions=["Tap back -> scr_restaurant_detail", "Tap Proceed to Checkout -> scr_checkout"],
                primary_cta="Proceed to Checkout • $10.34",
                secondary_actions=["Add More Items", "Apply Campus Voucher"],
                content_hierarchy=["Cart Items List", "Campus Drop Location Selector", "Bill Breakdown & Student Discount", "Checkout CTA"],
                layout=ScreenLayout(width=393, height=852, direction="vertical", padding_top=48, padding_bottom=40, padding_left=16, padding_right=16, gap=16),
                sections=[
                    ScreenSection(
                        section_id="sec_cart_items_list",
                        title="Your Order from Quad Noodle Bar",
                        direction="vertical",
                        gap=10,
                        components=[
                            ComponentInstanceSpec(
                                instance_id=f"inst_cart_item_{i}",
                                component_ref="cmp_entity_card",
                                name=f"Cart Item: {it['name']}",
                                content_data=it
                            ) for i, it in enumerate(content["active_cart"]["items"])
                        ]
                    ),
                    ScreenSection(
                        section_id="sec_drop_spot",
                        title="Campus Pickup Landmark",
                        direction="vertical",
                        gap=8,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_drop_selector",
                                component_ref="cmp_input_field",
                                name="Dorm Drop Point",
                                content_data={"label": "Drop Location", "value": content["active_cart"]["dorm_destination"]}
                            )
                        ]
                    ),
                    ScreenSection(
                        section_id="sec_bill_summary",
                        title="Student Pricing Breakdown",
                        direction="vertical",
                        gap=6,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_bill_card",
                                component_ref="cmp_entity_card",
                                name="Bill Summary Box",
                                content_data={
                                    "Subtotal": content["active_cart"]["subtotal"],
                                    "Student Discount": content["active_cart"]["student_discount"],
                                    "Delivery Fee": content["active_cart"]["delivery_fee"],
                                    "Total": content["active_cart"]["total"]
                                }
                            ),
                            ComponentInstanceSpec(
                                instance_id="inst_btn_to_checkout",
                                component_ref="cmp_btn_primary",
                                name="Checkout Button",
                                content_data={"label": f"Go to Checkout • {content['active_cart']['total']}"},
                                interactive_target_screen_id="scr_checkout"
                            )
                        ]
                    )
                ],
                prototype_destinations={"inst_btn_to_checkout": "scr_checkout"}
            )
            screens.append(scr_cart)

            # 5. Frictionless Checkout Screen
            scr_checkout = ScreenSpec(
                screen_id="scr_checkout",
                screen_name="Frictionless Payment & Confirmation",
                purpose="One-tap payment authorization via Apple Pay, Student Campus ID Card, or Credit Card.",
                user_goal="Safely complete payment with zero surprise fees.",
                entry_conditions=["Tap Checkout on Cart screen"],
                exit_actions=["Tap back -> scr_cart", "Pay Now -> scr_order_confirmation"],
                primary_cta="Slide to Pay • $10.34",
                secondary_actions=["Change Payment Method", "Add Courier Note"],
                content_hierarchy=["Payment Method Selector", "Delivery Contact Phone", "Order Total", "Slide to Pay Affordance"],
                layout=ScreenLayout(width=393, height=852, direction="vertical", padding_top=48, padding_bottom=40, padding_left=16, padding_right=16, gap=16),
                sections=[
                    ScreenSection(
                        section_id="sec_payment_methods",
                        title="Payment Method",
                        direction="vertical",
                        gap=10,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_apple_pay",
                                component_ref="cmp_btn_secondary",
                                name="Apple Pay Option",
                                content_data={"label": "Pay (Default)", "badge": "Fast"}
                            ),
                            ComponentInstanceSpec(
                                instance_id="inst_campus_card",
                                component_ref="cmp_btn_secondary",
                                name="Campus ID Cash Option",
                                content_data={"label": "Campus Card Cash ($42.50 Balance)"}
                            )
                        ]
                    ),
                    ScreenSection(
                        section_id="sec_checkout_confirm_action",
                        title="Final Authorize Order",
                        direction="vertical",
                        gap=12,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_btn_pay_confirm",
                                component_ref="cmp_btn_primary",
                                name="Confirm and Pay Button",
                                content_data={"label": "Confirm & Place Order • $10.34"},
                                interactive_target_screen_id="scr_order_confirmation"
                            )
                        ]
                    )
                ],
                prototype_destinations={"inst_btn_pay_confirm": "scr_order_confirmation"}
            )
            screens.append(scr_checkout)

            # 6. Order Confirmed Screen
            scr_confirmed = ScreenSpec(
                screen_id="scr_order_confirmation",
                screen_name="Order Confirmed & Kitchen Ticket",
                purpose="Provide immediate peace of mind, order number, kitchen prep timer, and tracking shortcut.",
                user_goal="Know order is received and see when it will arrive.",
                entry_conditions=["Successful payment completion"],
                exit_actions=["Tap Live Track -> scr_order_tracking", "Tap Home -> scr_home"],
                primary_cta="Live Track Delivery",
                secondary_actions=["View Receipt", "Back to Home"],
                content_hierarchy=["Success Animation Check", "Order #402 Number", "Kitchen Preparation Status", "Live ETA", "Track Button"],
                layout=ScreenLayout(width=393, height=852, direction="vertical", padding_top=64, padding_bottom=40, padding_left=16, padding_right=16, gap=20),
                sections=[
                    ScreenSection(
                        section_id="sec_conf_banner",
                        title="Success Confirmation",
                        direction="vertical",
                        gap=16,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_badge_success",
                                component_ref="cmp_status_badge",
                                name="Order Placed Badge",
                                content_data={"label": "✅ Order #402 Placed Successfully", "color": "success"}
                            ),
                            ComponentInstanceSpec(
                                instance_id="inst_conf_card",
                                component_ref="cmp_entity_card",
                                name="Prep Time Summary",
                                content_data={
                                    "title": "Kitchen is preparing your meal 🍜",
                                    "Estimated Delivery": "15-20 minutes",
                                    "Pickup PIN": content["active_cart"]["order_pin"],
                                    "Destination": content["active_cart"]["dorm_destination"]
                                }
                            ),
                            ComponentInstanceSpec(
                                instance_id="inst_btn_track_live",
                                component_ref="cmp_btn_primary",
                                name="Live Track Delivery Button",
                                content_data={"label": "Track Delivery Live 🚴"},
                                interactive_target_screen_id="scr_order_tracking"
                            )
                        ]
                    )
                ],
                prototype_destinations={"inst_btn_track_live": "scr_order_tracking"}
            )
            screens.append(scr_confirmed)

            # 7. Live Order Tracking Screen
            scr_tracking = ScreenSpec(
                screen_id="scr_order_tracking",
                screen_name="Live Campus Delivery Map & PIN",
                purpose="Display real-time GPS location of courier on campus pathways, ETA, and 4-digit pickup security PIN.",
                user_goal="Meet the courier right on time without standing in the cold.",
                entry_conditions=["Tap Live Track on Confirmation or Orders tab"],
                exit_actions=["Tap back -> scr_home", "Call/Message Courier"],
                primary_cta="Message Courier",
                secondary_actions=["Call Courier", "Help with Order"],
                content_hierarchy=["Interactive Campus Map", "Courier Name & Bike Icon", "Pickup PIN Code Card", "Milestone Stepper (Kitchen -> On the Way -> Arrived)"],
                layout=ScreenLayout(width=393, height=852, direction="vertical", padding_top=48, padding_bottom=40, padding_left=16, padding_right=16, gap=16),
                sections=[
                    ScreenSection(
                        section_id="sec_tracking_map",
                        title="Campus Courier Map View",
                        direction="vertical",
                        gap=12,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_map_card",
                                component_ref="cmp_entity_card",
                                name="Live Campus Map Simulator",
                                content_data={
                                    "map_status": "Courier approaching North Quad Dorm Gate",
                                    "courier_name": "Jordan P. (Bicycle)",
                                    "eta": "4 mins away",
                                    "pickup_pin": "PIN: 4821"
                                }
                            ),
                            ComponentInstanceSpec(
                                instance_id="inst_btn_msg_courier",
                                component_ref="cmp_btn_secondary",
                                name="Contact Courier Button",
                                content_data={"label": "💬 Message Courier: 'I am at the main door'"}
                            )
                        ]
                    )
                ],
                prototype_destinations={"inst_map_card": "scr_home"}
            )
            screens.append(scr_tracking)

        else:
            # SaaS Project Management Screens (Desktop 1280x900)
            # 1. Dashboard Overview
            scr_dashboard = ScreenSpec(
                screen_id="scr_dashboard",
                screen_name="Sprint Engineering Dashboard",
                purpose="Provide comprehensive visibility into active sprint progress, blocker alerts, and team bandwidth.",
                user_goal="Quickly identify blocked PRs and check overall sprint velocity.",
                entry_conditions=["User login", "Click Dashboard in sidebar"],
                exit_actions=["Click Kanban Board -> scr_kanban_board", "Click + New Task -> scr_create_task_modal"],
                primary_cta="+ New Task (C)",
                secondary_actions=["Filter My Tasks", "Export Sprint Report"],
                content_hierarchy=["Sprint Burndown Health", "High-Priority Blocker Cards", "Active PRs Pending Review", "Recent Team Commits"],
                layout=ScreenLayout(width=1280, height=900, direction="horizontal", padding_top=0, padding_bottom=0, padding_left=0, padding_right=0, gap=0),
                sections=[
                    ScreenSection(
                        section_id="sec_sidebar",
                        title="Persistent Left Sidebar",
                        direction="vertical",
                        gap=16,
                        layout_mode="fixed",
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_sidebar_nav",
                                component_ref="cmp_global_nav",
                                name="Global Sidebar",
                                content_data={"active": "Dashboard"},
                                interactive_target_screen_id="scr_kanban_board"
                            )
                        ]
                    ),
                    ScreenSection(
                        section_id="sec_main_content",
                        title="Main Dashboard View",
                        direction="vertical",
                        gap=24,
                        padding=32,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_sprint_summary",
                                component_ref="cmp_entity_card",
                                name="Sprint Burndown Metric Card",
                                content_data=content
                            ),
                            ComponentInstanceSpec(
                                instance_id="inst_btn_new_task",
                                component_ref="cmp_btn_primary",
                                name="Create Task Button",
                                content_data={"label": "+ Create Task (Press C)"},
                                interactive_target_screen_id="scr_create_task_modal"
                            )
                        ]
                    )
                ],
                prototype_destinations={"inst_sidebar_nav": "scr_kanban_board", "inst_btn_new_task": "scr_create_task_modal"}
            )
            screens.append(scr_dashboard)

            # 2. Kanban Board Screen
            scr_board = ScreenSpec(
                screen_id="scr_kanban_board",
                screen_name="Agile Sprint Kanban Board",
                purpose="Visual drag-and-drop workflow tracking across Backlog, Ready, In Progress, Review, and Done columns.",
                user_goal="Move tasks across stages and assign engineers with zero friction.",
                entry_conditions=["Click Sprint Board in sidebar"],
                exit_actions=["Click task card -> scr_task_detail", "Click Analytics -> scr_analytics"],
                primary_cta="+ Add Task to Column",
                secondary_actions=["Filter by Assignee", "Toggle Group by Epic"],
                content_hierarchy=["Board Header & Sprint Selector", "Filter & Search Bar", "Kanban Columns (Backlog, Dev, Review, Done)", "Task Cards with Story Points"],
                layout=ScreenLayout(width=1280, height=900, direction="horizontal", padding_top=0, padding_bottom=0, padding_left=0, padding_right=0, gap=0),
                sections=[
                    ScreenSection(
                        section_id="sec_board_content",
                        title="5-Column Kanban Board",
                        direction="horizontal",
                        gap=16,
                        padding=24,
                        components=[
                            ComponentInstanceSpec(
                                instance_id=f"inst_kanban_col_{col['id']}",
                                component_ref="cmp_entity_card",
                                name=f"Kanban Column: {col['title']}",
                                content_data=col
                            ) for col in content["columns"]
                        ]
                    )
                ],
                prototype_destinations={"inst_kanban_col_col_progress": "scr_task_detail"}
            )
            screens.append(scr_board)

            # 3. Task Detail & Edit Drawer Screen
            scr_detail = ScreenSpec(
                screen_id="scr_task_detail",
                screen_name="Task Specification & PR Traceability Drawer",
                purpose="Inspect task acceptance criteria, assignees, linked Git branches, PR review statuses, and comments.",
                user_goal="Review implementation requirements and link GitHub PR.",
                entry_conditions=["Click any task card on board or list"],
                exit_actions=["Close drawer -> scr_kanban_board", "Merge PR"],
                primary_cta="Move to PR In Review",
                secondary_actions=["Copy Branch Name", "Assign Reviewer"],
                content_hierarchy=["Task Key & Title", "Status & Story Points Dropdown", "Markdown Description", "Linked GitHub PR Status", "Discussion Thread"],
                layout=ScreenLayout(width=1280, height=900, direction="horizontal", padding_top=0, padding_bottom=0, padding_left=0, padding_right=0, gap=0),
                sections=[
                    ScreenSection(
                        section_id="sec_drawer_content",
                        title="Task Detail Drawer",
                        direction="vertical",
                        gap=16,
                        padding=32,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_task_detail_card",
                                component_ref="cmp_entity_card",
                                name="Task Detail Spec",
                                content_data=content["sample_tasks"][0]
                            ),
                            ComponentInstanceSpec(
                                instance_id="inst_btn_close_drawer",
                                component_ref="cmp_btn_secondary",
                                name="Close Drawer Button",
                                content_data={"label": "Close (Esc)"},
                                interactive_target_screen_id="scr_kanban_board"
                            )
                        ]
                    )
                ],
                prototype_destinations={"inst_btn_close_drawer": "scr_kanban_board"}
            )
            screens.append(scr_detail)

            # 4. Sprint Analytics Screen
            scr_analytics = ScreenSpec(
                screen_id="scr_analytics",
                screen_name="Sprint Velocity & Burndown Analytics",
                purpose="Visualize team velocity trends, cycle times, PR review latency, and completion forecasts.",
                user_goal="Evaluate sprint delivery health during retrospectives.",
                entry_conditions=["Click Analytics in sidebar"],
                exit_actions=["Return to Board -> scr_kanban_board"],
                primary_cta="Export Retrospective PDF",
                secondary_actions=["Switch Sprint", "Filter by Squad"],
                content_hierarchy=["Velocity Metric KPIs", "Burndown Chart", "Cycle Time Breakdown", "Contributor Impact Table"],
                layout=ScreenLayout(width=1280, height=900, direction="horizontal", padding_top=0, padding_bottom=0, padding_left=0, padding_right=0, gap=0),
                sections=[
                    ScreenSection(
                        section_id="sec_analytics_view",
                        title="Velocity Metrics Overview",
                        direction="vertical",
                        gap=20,
                        padding=32,
                        components=[
                            ComponentInstanceSpec(
                                instance_id="inst_velocity_card",
                                component_ref="cmp_entity_card",
                                name="Sprint Velocity Card",
                                content_data=content["velocity_metrics"]
                            ),
                            ComponentInstanceSpec(
                                instance_id="inst_btn_back_to_board",
                                component_ref="cmp_btn_secondary",
                                name="Back to Board",
                                content_data={"label": "← Back to Sprint Board"},
                                interactive_target_screen_id="scr_kanban_board"
                            )
                        ]
                    )
                ],
                prototype_destinations={"inst_btn_back_to_board": "scr_kanban_board"}
            )
            screens.append(scr_analytics)

        return screens
