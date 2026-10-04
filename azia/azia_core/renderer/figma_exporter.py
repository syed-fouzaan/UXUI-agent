"""
AZIA Figma Plugin Payload Exporter
Serializes operations and design specifications into production Figma Plugin API commands.
"""

import json
from typing import Dict, Any, List
from azia.azia_core.models.operations import FigmaOperation
from azia.azia_core.models.specification import ProductDesignSpecification


class FigmaExporter:
    """Exports operations and metadata as clean JSON consumable by the Figma Plugin."""

    def export_plugin_payload(
        self,
        spec: ProductDesignSpecification,
        operations: List[FigmaOperation]
    ) -> Dict[str, Any]:
        return {
            "type": "AZIA_RENDER_PRODUCT",
            "metadata": {
                "product_id": spec.metadata.product_id,
                "product_name": spec.metadata.product_name,
                "category": spec.metadata.product_category,
                "generation_id": spec.metadata.generation_id,
                "managed_by": spec.metadata.managed_by,
                "total_operations": len(operations),
                "total_screens": len(spec.screens),
                "total_components": len(spec.component_registry.components),
            },
            "design_tokens": spec.design_system.model_dump(),
            "operations": [op.model_dump() for op in operations],
            "audit_findings": [f.model_dump() for f in spec.audit_report.findings] if spec.audit_report else []
        }
