"""
AZIA Content Intelligence Engine
Generates hyper-realistic, domain-specific copy and interface data.
Explicitly bans "Lorem Ipsum", generic "Card Title", and dummy placeholders.
"""

from typing import Dict, Any, List
from azia.azia_core.intelligence.requirement_engine import RequirementAnalysis


class ContentEngine:
    """Generates authentic microcopy, labels, entities, and prices."""

    def generate_domain_content(self, analysis: RequirementAnalysis) -> Dict[str, Any]:
        category = analysis.product_category.lower()

        if "food" in category:
            return {
                "tagline": "Fuel Your Campus Grind 🎓 Fast, Budget-Friendly Dorm Delivery",
                "quick_filters": [
                    {"label": "Under $10 💰", "active": True},
                    {"label": "⚡ Under 20 Mins", "active": False},
                    {"label": "🌱 Plant-Based", "active": False},
                    {"label": "Late Night 🌙", "active": False},
                    {"label": "Top Rated ⭐", "active": False},
                ],
                "restaurants": [
                    {
                        "id": "rest_01",
                        "name": "Quad Noodle Bar & Dumplings",
                        "badge": "Student Favorite 🔥",
                        "cuisine": "Pan-Asian • Noodles & Bowls",
                        "rating": "4.9 (1.2k+ students)",
                        "delivery_time": "15–20 min",
                        "delivery_fee": "FREE campus drop",
                        "price_level": "$",
                        "popular_dish": "Crispy Chili Garlic Noodles with Tofu",
                        "price": "$8.49",
                        "dorm_landmark": "North Quad Bike Rack Locker",
                    },
                    {
                        "id": "rest_02",
                        "name": "Varsity Burrito Co.",
                        "badge": "Buy 1 Get 50% Off 🌯",
                        "cuisine": "Mexican Grill • Bowls & Tacos",
                        "rating": "4.8 (890)",
                        "delivery_time": "20–25 min",
                        "delivery_fee": "$0.99",
                        "price_level": "$",
                        "popular_dish": "Mega Carnitas Bowl + Fresh Guac",
                        "price": "$9.95",
                        "dorm_landmark": "South Quad Central Arch",
                    },
                    {
                        "id": "rest_03",
                        "name": "Library Street Woodfired Pizza",
                        "badge": "Midnight Slice Deal 🍕",
                        "cuisine": "Italian • Artisanal Slices",
                        "rating": "4.7 (2.4k)",
                        "delivery_time": "25–30 min",
                        "delivery_fee": "FREE over $12",
                        "price_level": "$$",
                        "popular_dish": "Hot Honey Pepperoni Personal Pie",
                        "price": "$11.50",
                        "dorm_landmark": "Engineering Hall Entrance",
                    }
                ],
                "active_cart": {
                    "restaurant_name": "Quad Noodle Bar & Dumplings",
                    "items": [
                        {"name": "Crispy Chili Garlic Noodles", "qty": 1, "customization": "Spicy Level 3, Extra Scallions", "price": "$8.49"},
                        {"name": "Pan-Fried Gyoza (4 pcs)", "qty": 1, "customization": "Sweet Soy Dip", "price": "$3.50"}
                    ],
                    "subtotal": "$11.99",
                    "student_discount": "-$2.50 (CampusPromo2026)",
                    "delivery_fee": "$0.00",
                    "estimated_tax": "$0.85",
                    "total": "$10.34",
                    "dorm_destination": "Prentice Dorm Tower B - Ground Lobby",
                    "courier_eta": "14 minutes remaining",
                    "order_pin": "4821"
                }
            }

        else:
            # SaaS Project Management
            return {
                "workspace_title": "SprintFlow • Core Platform Eng Team",
                "active_sprint": "Sprint 34: Auth v2 & Realtime Webhooks",
                "sprint_status": "Day 6 of 10 • 78% on track",
                "burndown_summary": "42 of 58 Story Points Completed • 4 Blocked",
                "columns": [
                    {"id": "col_backlog", "title": "Backlog (8)", "color": "#64748B"},
                    {"id": "col_ready", "title": "Ready for Dev (4)", "color": "#3B82F6"},
                    {"id": "col_progress", "title": "In Progress (5)", "color": "#F59E0B"},
                    {"id": "col_review", "title": "PR In Review (3)", "color": "#8B5CF6"},
                    {"id": "col_done", "title": "Done & Merged (14)", "color": "#10B981"}
                ],
                "sample_tasks": [
                    {
                        "key": "ENG-402",
                        "title": "Migrate JWT refresh token rotation to Redis cluster",
                        "priority": "P0 Urgent",
                        "priority_color": "#EF4444",
                        "assignee": "Elena Rostova",
                        "assignee_initials": "ER",
                        "points": "5 pts",
                        "branch": "feat/redis-jwt-rotation",
                        "pr_status": "PR #128 opened • 2 approvals"
                    },
                    {
                        "key": "ENG-409",
                        "title": "Implement rate limiting middleware for public GraphQL gateway",
                        "priority": "P1 High",
                        "priority_color": "#F59E0B",
                        "assignee": "Marcus Vance",
                        "assignee_initials": "MV",
                        "points": "3 pts",
                        "branch": "fix/graphql-rate-limiter",
                        "pr_status": "CI passing • Tests 100%"
                    },
                    {
                        "key": "ENG-415",
                        "title": "Add telemetry span for Figma Plugin WebSocket handshake latency",
                        "priority": "P2 Normal",
                        "priority_color": "#3B82F6",
                        "assignee": "Samir Patel",
                        "assignee_initials": "SP",
                        "points": "2 pts",
                        "branch": "chore/mcp-telemetry",
                        "pr_status": "Draft PR"
                    }
                ],
                "velocity_metrics": {
                    "avg_velocity": "54 pts/sprint",
                    "cycle_time": "1.8 days",
                    "pr_merge_time": "4.2 hrs"
                }
            }
