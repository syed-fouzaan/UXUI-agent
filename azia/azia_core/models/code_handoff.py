"""
AZIA Production Code Handoff Models
Structures generated source code files for React + Tailwind, SwiftUI, and W3C Design Tokens.
"""

from enum import Enum
from typing import List, Dict, Any
from pydantic import BaseModel, Field


class FrameworkType(str, Enum):
    REACT_TAILWIND = "REACT_TAILWIND"
    SWIFTUI = "SWIFTUI"
    W3C_TOKENS = "W3C_TOKENS"


class GeneratedSourceFile(BaseModel):
    """An individual production source code file."""
    filename: str
    relative_path: str
    language: str  # tsx, swift, json, css
    description: str
    code_content: str


class GeneratedCodeBundle(BaseModel):
    """Bundle of production components and design tokens ready for development."""
    product_name: str
    framework: FrameworkType
    files: List[GeneratedSourceFile] = Field(default_factory=list)
    install_instructions: str
    package_dependencies: List[str] = Field(default_factory=list)
