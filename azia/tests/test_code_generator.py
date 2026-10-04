"""
Unit tests for CodeGenerator (React + Tailwind, SwiftUI, W3C DTCG Tokens).
"""

import json
import pytest
from azia.azia_core.orchestrator import AutonomousDesignPipeline
from azia.azia_core.intelligence.code_generator import CodeGenerator
from azia.azia_core.models.code_handoff import FrameworkType


def test_react_tailwind_code_generation():
    pipeline = AutonomousDesignPipeline()
    code_gen = CodeGenerator()

    spec, _, _, _ = pipeline.design_product(
        "Build a modern food delivery app for college students"
    )

    bundle = code_gen.generate_react_tailwind(spec)
    assert bundle.framework == FrameworkType.REACT_TAILWIND
    assert len(bundle.files) >= 2

    app_tsx = next(f for f in bundle.files if f.filename == "App.tsx")
    assert "import React" in app_tsx.code_content
    assert "setActiveScreen" in app_tsx.code_content
    assert spec.design_system.colors.primary.hex in app_tsx.code_content

    tailwind_js = next(f for f in bundle.files if f.filename == "tailwind.config.js")
    assert "theme:" in tailwind_js.code_content


def test_swiftui_code_generation():
    pipeline = AutonomousDesignPipeline()
    code_gen = CodeGenerator()

    spec, _, _, _ = pipeline.design_product(
        "Build a modern food delivery app for college students"
    )

    bundle = code_gen.generate_swiftui(spec)
    assert bundle.framework == FrameworkType.SWIFTUI
    assert len(bundle.files) >= 1

    swift_file = bundle.files[0]
    assert "import SwiftUI" in swift_file.code_content
    assert "struct ContentView: View" in swift_file.code_content
    assert "@State private var selectedScreen" in swift_file.code_content


def test_w3c_tokens_export():
    pipeline = AutonomousDesignPipeline()
    code_gen = CodeGenerator()

    spec, _, _, _ = pipeline.design_product(
        "Build a modern food delivery app for college students"
    )

    token_file = code_gen.generate_w3c_tokens(spec)
    assert token_file.filename == "tokens.json"

    parsed = json.loads(token_file.code_content)
    assert "color" in parsed
    assert "spacing" in parsed
    assert parsed["color"]["primary"]["$value"] == spec.design_system.colors.primary.hex
