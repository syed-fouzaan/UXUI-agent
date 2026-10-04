"""
AZIA Design System Ingestion Models
Structures incoming design system definitions from Figma Tokens Studio, W3C DTCG, CSS variables, and Tailwind themes.
"""

from enum import Enum
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class DesignSystemSourceFormat(str, Enum):
    FIGMA_TOKENS_STUDIO = "FIGMA_TOKENS_STUDIO"
    W3C_DTCG = "W3C_DTCG"
    CSS_VARIABLES = "CSS_VARIABLES"
    TAILWIND_THEME = "TAILWIND_THEME"


class IngestedToken(BaseModel):
    name: str
    category: str  # color, typography, spacing, radius, shadow
    value: str
    original_path: str


class ComponentMappingRule(BaseModel):
    external_component_name: str
    external_figma_key: Optional[str] = None
    target_semantic_type: str
    property_mappings: Dict[str, str] = Field(default_factory=dict)


class DesignSystemImportResult(BaseModel):
    success: bool = True
    system_name: str
    source_format: DesignSystemSourceFormat
    total_tokens_imported: int
    color_tokens_count: int
    typography_tokens_count: int
    spacing_tokens_count: int
    component_mappings: List[ComponentMappingRule] = Field(default_factory=list)
    import_warnings: List[str] = Field(default_factory=list)
