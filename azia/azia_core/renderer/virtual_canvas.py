"""
AZIA Virtual Figma Document Engine
Simulates the Figma document tree in memory, maintaining Auto Layout constraints,
components, instances, text nodes, sticky notes, connectors, and non-destructive ownership metadata.
"""

from typing import Dict, List, Optional, Any
from azia.azia_core.models.operations import FigmaOperation, FigmaOperationType


class VirtualFigmaNode:
    """Represents a node in the Figma document scene graph."""
    def __init__(
        self,
        node_id: str,
        name: str,
        node_type: str,
        parent_id: Optional[str] = None
    ):
        self.id = node_id
        self.name = name
        self.type = node_type
        self.parent_id = parent_id
        self.children: List['VirtualFigmaNode'] = []
        self.x: int = 0
        self.y: int = 0
        self.width: int = 100
        self.height: int = 100
        self.layout_mode: str = "NONE"  # HORIZONTAL, VERTICAL, NONE
        self.padding_top: int = 0
        self.padding_bottom: int = 0
        self.padding_left: int = 0
        self.padding_right: int = 0
        self.item_spacing: int = 0
        self.corner_radius: int = 0
        self.fills: List[Dict[str, Any]] = []
        self.strokes: List[Dict[str, Any]] = []
        self.characters: str = ""
        self.plugin_data: Dict[str, str] = {}
        self.reactions: List[Dict[str, Any]] = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "parent_id": self.parent_id,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "layout_mode": self.layout_mode,
            "padding": {
                "top": self.padding_top,
                "bottom": self.padding_bottom,
                "left": self.padding_left,
                "right": self.padding_right
            },
            "item_spacing": self.item_spacing,
            "corner_radius": self.corner_radius,
            "fills": self.fills,
            "characters": self.characters,
            "plugin_data": self.plugin_data,
            "reactions": self.reactions,
            "children": [c.to_dict() for c in self.children]
        }


class VirtualFigmaCanvas:
    """The local Figma document emulator."""

    def __init__(self):
        self.nodes_by_id: Dict[str, VirtualFigmaNode] = {}
        self.root_pages: List[VirtualFigmaNode] = []
        self.history_snapshots: List[Dict[str, Any]] = []

    def execute_operations(self, operations: List[FigmaOperation]) -> int:
        """Deterministically renders a list of operations into the virtual canvas."""
        executed_count = 0

        for op in operations:
            parent = self.nodes_by_id.get(op.parent_id) if op.parent_id else None

            if op.op_type == FigmaOperationType.CREATE_PAGE:
                node = VirtualFigmaNode(op.target_id, op.name, "PAGE")
                node.plugin_data["managed_by"] = op.managed_by
                node.plugin_data["generation_id"] = op.generation_id or ""
                self.nodes_by_id[op.target_id] = node
                self.root_pages.append(node)
                executed_count += 1

            elif op.op_type == FigmaOperationType.CREATE_SECTION:
                node = VirtualFigmaNode(op.target_id, op.name, "SECTION", op.parent_id)
                node.x = op.payload.get("x", 0)
                node.y = op.payload.get("y", 0)
                node.width = op.payload.get("width", 1200)
                node.height = op.payload.get("height", 800)
                node.plugin_data["managed_by"] = op.managed_by
                self.nodes_by_id[op.target_id] = node
                if parent:
                    parent.children.append(node)
                executed_count += 1

            elif op.op_type == FigmaOperationType.CREATE_STICKY_NOTE:
                node = VirtualFigmaNode(op.target_id, op.name, "STICKY", op.parent_id)
                node.x = op.payload.get("x", 0)
                node.y = op.payload.get("y", 0)
                node.characters = op.payload.get("content", "")
                node.fills = [{"type": "SOLID", "color": op.payload.get("color", "YELLOW")}]
                node.plugin_data["managed_by"] = op.managed_by
                self.nodes_by_id[op.target_id] = node
                if parent:
                    parent.children.append(node)
                executed_count += 1

            elif op.op_type == FigmaOperationType.CREATE_COMPONENT:
                node = VirtualFigmaNode(op.target_id, op.name, "COMPONENT", op.parent_id)
                node.width = op.payload.get("width", 120)
                node.height = op.payload.get("height", 44)
                node.layout_mode = "HORIZONTAL" if op.payload.get("direction") == "horizontal" else "VERTICAL"
                node.item_spacing = op.payload.get("gap", 8)
                node.corner_radius = op.payload.get("radius", 8)
                node.plugin_data["managed_by"] = op.managed_by
                self.nodes_by_id[op.target_id] = node
                if parent:
                    parent.children.append(node)
                executed_count += 1

            elif op.op_type == FigmaOperationType.CREATE_SCREEN:
                node = VirtualFigmaNode(op.target_id, op.name, "FRAME", op.parent_id)
                node.x = op.payload.get("x", 0)
                node.y = op.payload.get("y", 0)
                node.width = op.payload.get("width", 393)
                node.height = op.payload.get("height", 852)
                node.layout_mode = "VERTICAL"
                node.padding_top = op.payload.get("padding_top", 44)
                node.padding_bottom = op.payload.get("padding_bottom", 34)
                node.padding_left = op.payload.get("padding_x", 16)
                node.padding_right = op.payload.get("padding_x", 16)
                node.item_spacing = op.payload.get("gap", 16)
                node.fills = [{"type": "SOLID", "color_hex": op.payload.get("bg_hex", "#FFFFFF")}]
                node.plugin_data["managed_by"] = op.managed_by
                node.plugin_data["screen_id"] = op.target_id
                self.nodes_by_id[op.target_id] = node
                if parent:
                    parent.children.append(node)
                executed_count += 1

            elif op.op_type == FigmaOperationType.CREATE_AUTO_LAYOUT:
                node = VirtualFigmaNode(op.target_id, op.name, "FRAME", op.parent_id)
                direction = op.payload.get("direction", "vertical").upper()
                node.layout_mode = "HORIZONTAL" if direction == "HORIZONTAL" else "VERTICAL"
                node.item_spacing = op.payload.get("gap", 12)
                node.padding_left = op.payload.get("padding", 0)
                node.padding_right = op.payload.get("padding", 0)
                node.plugin_data["managed_by"] = op.managed_by
                self.nodes_by_id[op.target_id] = node
                if parent:
                    parent.children.append(node)
                executed_count += 1

            elif op.op_type == FigmaOperationType.CREATE_INSTANCE:
                node = VirtualFigmaNode(op.target_id, op.name, "INSTANCE", op.parent_id)
                node.plugin_data["master_component"] = op.payload.get("master_component_id", "")
                node.plugin_data["managed_by"] = op.managed_by
                node.plugin_data["content"] = str(op.payload.get("content_data", {}))
                self.nodes_by_id[op.target_id] = node
                if parent:
                    parent.children.append(node)
                executed_count += 1

            elif op.op_type == FigmaOperationType.CONNECT_PROTOTYPE:
                # Attach reaction to source screen
                src = self.nodes_by_id.get(op.payload.get("source_screen_id", ""))
                if src:
                    src.reactions.append({
                        "trigger": op.payload.get("trigger", "ON_CLICK"),
                        "destination_id": op.payload.get("target_screen_id", ""),
                        "animation": op.payload.get("animation", "SLIDE_IN_RIGHT")
                    })
                executed_count += 1

        return executed_count

    def find_nodes_by_ownership(self, managed_by: str = "autonomous-design-mcp") -> List[VirtualFigmaNode]:
        """Filters nodes tagged by autonomous design engine, enabling non-destructive operations."""
        return [
            n for n in self.nodes_by_id.values()
            if n.plugin_data.get("managed_by") == managed_by
        ]

    def rollback_generation(self, generation_id: str) -> int:
        """Removes only nodes created in a specific generation run, preserving user work."""
        to_delete = [
            nid for nid, n in self.nodes_by_id.items()
            if n.plugin_data.get("generation_id") == generation_id
        ]
        for nid in to_delete:
            del self.nodes_by_id[nid]
        return len(to_delete)
