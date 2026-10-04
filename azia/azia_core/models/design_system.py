"""
AZIA Design System Models
Comprehensive token architecture based on the 8pt grid, WCAG 2.1 AA/AAA accessibility standards,
modern typographic hierarchy, and semantic color scales.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class ColorToken(BaseModel):
    """Semantic color token with accessibility metadata."""
    name: str = Field(description="e.g. primary, surface, text-primary")
    hex: str = Field(description="#RRGGBB or #RRGGBBAA")
    role: str = Field(description="background, surface, interactive, text, border, feedback")
    contrast_ratio_on_bg: float = Field(default=4.5, description="Calculated contrast against main background")
    wcag_aa_compliant: bool = Field(default=True)
    wcag_aaa_compliant: bool = Field(default=False)


class ColorPalette(BaseModel):
    """Full semantic color system."""
    primary: ColorToken
    primary_hover: ColorToken
    secondary: ColorToken
    accent: ColorToken
    background: ColorToken
    surface: ColorToken
    surface_elevated: ColorToken
    text_primary: ColorToken
    text_secondary: ColorToken
    text_muted: ColorToken
    border_subtle: ColorToken
    border_focus: ColorToken
    success: ColorToken
    warning: ColorToken
    error: ColorToken


class TypographyToken(BaseModel):
    """A distinct typographic style."""
    name: str = Field(description="display, h1, h2, h3, body_lg, body_md, body_sm, caption, button")
    font_family: str = Field(default="Inter, -apple-system, sans-serif")
    font_size: int = Field(description="Size in px")
    line_height: int = Field(description="Line height in px")
    font_weight: int = Field(default=400, description="400, 500, 600, 700")
    letter_spacing: float = Field(default=0.0, description="Letter spacing in em or px")


class TypographyScale(BaseModel):
    """Complete typography hierarchy."""
    display: TypographyToken
    h1: TypographyToken
    h2: TypographyToken
    h3: TypographyToken
    body_lg: TypographyToken
    body_md: TypographyToken
    body_sm: TypographyToken
    caption: TypographyToken
    button_label: TypographyToken
    code: TypographyToken


class SpacingScale(BaseModel):
    """Strict 8-point spatial system (with 4px half-step for micro-elements)."""
    xxs: int = Field(default=2, description="2px border/hairline spacing")
    xs: int = Field(default=4, description="4px half-grid micro spacing")
    sm: int = Field(default=8, description="8px standard small element spacing")
    md: int = Field(default=16, description="16px standard component internal padding")
    lg: int = Field(default=24, description="24px card and section spacing")
    xl: int = Field(default=32, description="32px major section gap")
    xxl: int = Field(default=48, description="48px page block spacing")
    xxxl: int = Field(default=64, description="64px landmark / hero spacing")


class RadiusScale(BaseModel):
    """Border radius tokens."""
    none: int = Field(default=0)
    xs: int = Field(default=4)
    sm: int = Field(default=8)
    md: int = Field(default=12)
    lg: int = Field(default=16)
    xl: int = Field(default=24)
    full: int = Field(default=9999, description="Pill / circular radius")


class ShadowToken(BaseModel):
    """Elevation shadow token."""
    name: str = Field(description="none, sm, md, lg, xl")
    x: int = 0
    y: int = 2
    blur: int = 8
    spread: int = 0
    color: str = "rgba(0, 0, 0, 0.08)"
    css_box_shadow: str = "0 2px 8px rgba(0, 0, 0, 0.08)"


class DesignSystemTokens(BaseModel):
    """Unified Design System tokens specification."""
    system_name: str = Field(default="AZIA Cohesive Design Tokens")
    platform: str = Field(default="mobile", description="mobile, web, tablet, desktop")
    theme_mode: str = Field(default="light", description="light, dark")
    style_direction: str = Field(default="modern", description="modern, minimal, enterprise, playful, premium")
    colors: ColorPalette
    typography: TypographyScale
    spacing: SpacingScale = Field(default_factory=SpacingScale)
    radius: RadiusScale = Field(default_factory=RadiusScale)
    shadows: Dict[str, ShadowToken] = Field(default_factory=dict)
    grid_columns: int = Field(default=4, description="4 for mobile, 12 for desktop")
    container_width: int = Field(default=393, description="393 for mobile, 1280 for desktop")
