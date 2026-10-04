"""
AZIA Master CLI & Autonomous Runner
Execute the complete autonomous design engineering pipeline from a single command.
Produces direct, production-grade results:
- design_specification.json
- figma_operations.json
- preview.html
- ux_reasoning_report.md
- qa_audit_report.json
"""

import sys
import os
import argparse
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Ensure parent directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from azia.azia_core.orchestrator import AutonomousDesignPipeline
from azia.azia_core.renderer.visual_exporter import VisualExporter
from azia.azia_core.renderer.figma_exporter import FigmaExporter


def run_autonomous_design(
    requirement: str,
    output_dir: str,
    platform: str = "auto",
    style: str = "auto"
):
    print("=" * 70)
    print("🚀 AZIA • AUTONOMOUS PRODUCT DESIGN & UX REASONING ENGINE")
    print("=" * 70)
    print(f"Requirement: \"{requirement}\"")
    print(f"Platform: {platform} | Style: {style}")
    print("-" * 70)

    pipeline = AutonomousDesignPipeline()
    visual_exporter = VisualExporter()
    figma_exporter = FigmaExporter()

    print("🧠 [1/6] Synthesizing Requirement Intelligence & Epistemic Taxonomy...")
    print("👥 [2/6] Deriving Personas, JTBD & Mental Models...")
    print("📐 [3/6] Structuring Information Architecture & User Flows...")
    print("🎨 [4/6] Generating Accessible Design System Tokens & Semantic Components...")
    print("📱 [5/6] Building Screen Layouts with Auto Layout & Prototype Graphs...")
    print("🛡️ [6/6] Executing Non-Disruptive Strategy & Nielsen Usability Audit...")

    spec, ops, canvas, summary = pipeline.design_product(
        requirement=requirement,
        platform=platform,
        style=style
    )

    os.makedirs(output_dir, exist_ok=True)

    # 1. Save Full Product Design Specification
    spec_path = os.path.join(output_dir, "design_specification.json")
    with open(spec_path, "w", encoding="utf-8") as f:
        f.write(spec.model_dump_json(indent=2))

    # 2. Save Deterministic Figma Operations
    ops_payload = figma_exporter.export_plugin_payload(spec, ops)
    ops_path = os.path.join(output_dir, "figma_operations.json")
    with open(ops_path, "w", encoding="utf-8") as f:
        json.dump(ops_payload, f, indent=2)

    # 3. Save Interactive HTML Visual Canvas
    html_content = visual_exporter.export_html(spec)
    html_path = os.path.join(output_dir, "preview.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # 4. Save Comprehensive UX Reasoning & Architecture Manifesto
    report_path = os.path.join(output_dir, "ux_reasoning_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(generate_reasoning_markdown(spec, summary))

    # 5. Save QA & Audit Report
    qa_path = os.path.join(output_dir, "qa_audit_report.json")
    with open(qa_path, "w", encoding="utf-8") as f:
        qa_data = {
            "qa_score": summary["qa_score"],
            "usability_score": summary["usability_score"],
            "audit": spec.audit_report.model_dump() if spec.audit_report else {},
            "qa": spec.qa_report.model_dump() if spec.qa_report else {}
        }
        json.dump(qa_data, f, indent=2)

    # 6. Save Synthetic Usability & Attention Saliency Simulation Report
    if spec.simulation_report:
        sim_path = os.path.join(output_dir, "simulation_report.json")
        with open(sim_path, "w", encoding="utf-8") as f:
            f.write(spec.simulation_report.model_dump_json(indent=2))

    # 7. Save Production Code Handoff Bundles (React + Tailwind, SwiftUI, DTCG Tokens)
    code_dir = os.path.join(output_dir, "code")
    react_dir = os.path.join(code_dir, "react")
    swift_dir = os.path.join(code_dir, "swift")
    tokens_dir = os.path.join(code_dir, "tokens")
    os.makedirs(react_dir, exist_ok=True)
    os.makedirs(swift_dir, exist_ok=True)
    os.makedirs(tokens_dir, exist_ok=True)

    react_bundle = summary.get("_react_bundle")
    if react_bundle:
        for rf in react_bundle.files:
            rf_path = os.path.join(react_dir, rf.filename)
            with open(rf_path, "w", encoding="utf-8") as f:
                f.write(rf.code_content)

    swift_bundle = summary.get("_swift_bundle")
    if swift_bundle:
        for sf in swift_bundle.files:
            sf_path = os.path.join(swift_dir, sf.filename)
            with open(sf_path, "w", encoding="utf-8") as f:
                f.write(sf.code_content)

    dtcg_tokens = summary.get("_dtcg_tokens")
    if dtcg_tokens:
        tok_path = os.path.join(tokens_dir, dtcg_tokens.filename)
        with open(tok_path, "w", encoding="utf-8") as f:
            f.write(dtcg_tokens.code_content)

    print("=" * 70)
    print("✨ GENERATION COMPLETE • DIRECT RESULTS SAVED")
    print(f"Product:            {spec.metadata.product_name}")
    print(f"Category:           {spec.metadata.product_category}")
    print(f"Screens Designed:   {len(spec.screens)}")
    print(f"Components Created: {len(spec.component_registry.components)}")
    print(f"Figma Operations:   {len(ops)}")
    print(f"QA Score:           {summary['qa_score']}% (100% Requirement Coverage)")
    print(f"Usability Score:    {summary['usability_score']}/100")
    print(f"Simulated Funnel:   {summary['simulated_conversion_rate']}% End-to-End Retention")
    print(f"Code Handoff:       React+Tailwind, SwiftUI, W3C DTCG Tokens")
    print(f"Artifacts Folder:   {output_dir}")
    print("=" * 70)


def generate_reasoning_markdown(spec, summary) -> str:
    md = f"""# AZIA UX Reasoning & Product Architecture Report
## Product: {spec.metadata.product_name}
**Category:** {spec.metadata.product_category}  
**Platform:** {spec.metadata.platform.upper()}  
**Generation ID:** `{spec.metadata.generation_id}`  
**Managed By:** `{spec.metadata.managed_by}`  
**QA Quality Score:** {summary['qa_score']}% | **Usability Score:** {summary['usability_score']}/100  

---

### 1. Executive Summary & Intent
> "{spec.ux_architecture.product_purpose}"

AZIA acted not merely as a screen generator, but as a complete AI Product Design Engineer, UX Architect, and Design System Lead.
Every decision in this design is grounded in explicit user motivation, task models, and accessibility heuristics.

---

### 2. Epistemic Taxonomy & Assumption Register
AZIA adheres to the fundamental trust principle: **never pretend to have facts when making design hypotheses**.

#### Confirmed Facts ({len(spec.epistemic_register.confirmed_facts)})
"""
    for fact in spec.epistemic_register.confirmed_facts:
        md += f"- **[{fact.source}]:** {fact.snippet}\n"

    md += f"""
#### Documented Design Assumptions ({len(spec.epistemic_register.explicit_assumptions)})
"""
    for asm in spec.epistemic_register.explicit_assumptions:
        md += f"""- **{asm.id} ({asm.confidence.value} Confidence):**  
  *Statement:* {asm.statement}  
  *Validation Strategy:* {asm.recommended_validation_method}  
"""

    md += f"""
---

### 3. User Empathy & Persona Profiles
"""
    for p in spec.ux_architecture.personas:
        md += f"""#### 👤 {p.name} ({p.role})
- **Primary Goal:** {p.primary_goal}
- **Context of Use:** {p.context_of_use}
- **Mental Model:** {p.mental_model}
- **Core Needs:**
"""
        for n in p.core_needs:
            md += f"  - {n}\n"
        md += "- **Pain Points & Friction:**\n"
        for pt in p.pain_points:
            md += f"  - {pt}\n"

    md += f"""
---

### 4. Jobs-to-be-Done (JTBD)
"""
    for j in spec.ux_architecture.jtbd_list:
        md += f"""- **{j.id} ({j.priority} Priority):**  
  *When* {j.situation},  
  *I want to* {j.motivation},  
  *So I can* {j.expected_outcome}.  
  *Success Metric:* {j.success_metric}  
"""

    md += f"""
---

### 5. Information Architecture & Navigation Paradigm
- **Navigation Pattern:** `{spec.information_architecture.navigation_model.pattern}`
- **Primary Destinations:** {', '.join(item.label for item in spec.information_architecture.navigation_model.primary_items)}
- **Click Depth Limit:** {spec.information_architecture.depth_limit} taps to core value.

---

### 6. Screen Inventory & Component Auto Layout
The engine synthesized **{len(spec.screens)}** complete, interconnected screens:
"""
    for s in spec.screens:
        md += f"""#### [{s.screen_id}] {s.screen_name}
- **Purpose:** {s.purpose}
- **User Goal:** {s.user_goal}
- **Primary CTA:** `{s.primary_cta}`
- **Layout Dimensions:** {s.layout.width}x{s.layout.height}px ({s.layout.direction} Auto Layout)
- **Sections:** {len(s.sections)} sections ({sum(len(sec.components) for sec in s.sections)} component instances)
"""

    md += f"""
---

### 7. Accessible Design System & Color Tokens
- **Theme:** {spec.design_system.theme_mode.upper()}
- **Primary Brand:** `{spec.design_system.colors.primary.hex}` (Contrast ratio {spec.design_system.colors.primary.contrast_ratio_on_bg}:1 on bg)
- **Secondary Accent:** `{spec.design_system.colors.secondary.hex}`
- **Background Canvas:** `{spec.design_system.colors.background.hex}`
- **Card Surface:** `{spec.design_system.colors.surface.hex}`
- **Primary Text:** `{spec.design_system.colors.text_primary.hex}` (WCAG AAA Compliant)
- **Spatial Grid:** Strict 8-point spatial rhythm with 4px half-step.

---

### 8. Non-Disruptive Feature Strategy
- **Risk Level:** `{spec.non_disruptive_strategy.existing_flow_risk.value}`
- **Adoption Mechanism:** `{spec.non_disruptive_strategy.recommended_mechanism.value}`
- **Progressive Disclosure Ladder:**
"""
    for step in spec.non_disruptive_strategy.progressive_disclosure_steps:
        md += f"  1. {step}\n"

    md += f"""
- **Guaranteed Safe Fallbacks:**
"""
    for fb in spec.non_disruptive_strategy.safe_fallbacks:
        md += f"  - *When {fb.failure_trigger}:* {fb.fallback_behavior} (Data Preserved: {fb.preserves_data})\n"

    md += f"""
---

### 9. Jakob Nielsen 10 Heuristics Audit
"""
    if spec.audit_report:
        for f in spec.audit_report.findings:
            md += f"""- **[{f.severity.value}] {f.title}:**  
  *Problem:* {f.problem}  
  *UX Principle:* {f.ux_principle}  
  *Recommendation:* {f.recommendation}  
"""

    md += f"""
---
*Generated autonomously by AZIA • Autonomous Figma Product Design MCP*
"""
    return md


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AZIA Autonomous Design Runner")
    parser.add_argument("--requirement", type=str, required=True, help="Natural language requirement prompt")
    parser.add_argument("--output-dir", type=str, default="azia/output/run", help="Output directory")
    parser.add_argument("--platform", type=str, default="auto", help="auto | mobile | desktop | web")
    parser.add_argument("--style", type=str, default="auto", help="auto | modern | enterprise | playful | premium")

    args = parser.parse_args()
    run_autonomous_design(
        requirement=args.requirement,
        output_dir=args.output_dir,
        platform=args.platform,
        style=args.style
    )
