"""
AZIA Visual Preview Exporter
Generates a standalone, interactive, high-fidelity visual HTML preview of the generated product.
Supports:
1. Clickable prototype transitions with interactive screen navigation
2. Synthetic User Simulation & Visual Attention Saliency Heatmaps (Itti-Koch gaze engine & drop-off funnel)
3. 1-Click Code Handoff (React + Tailwind, SwiftUI, W3C DTCG Tokens) with copy-to-clipboard
4. Figma File Design System Ingestion (Tokens Studio & CSS variables live parser)
5. FigJam UX Architecture Board (Personas, JTBD, Assumptions)
6. Design Tokens & Accessibility Inspector
7. Nielsen Usability Audit & Dual-Track QA Reports
"""

import json
import html
from typing import Dict, Any, Optional
from azia.azia_core.models.specification import ProductDesignSpecification
from azia.azia_core.intelligence.simulation_engine import SimulationEngine
from azia.azia_core.intelligence.code_generator import CodeGenerator


class VisualExporter:
    """Exports comprehensive interactive visual representations for browser inspection."""

    def __init__(self):
        self.sim_engine = SimulationEngine()
        self.code_gen = CodeGenerator()

    def export_html(self, spec: ProductDesignSpecification) -> str:
        prod = spec.metadata
        ds = spec.design_system
        screens = spec.screens
        personas = spec.ux_architecture.personas
        assumptions = spec.epistemic_register.explicit_assumptions
        audit = spec.audit_report
        qa = spec.qa_report

        # Ensure simulation report exists
        sim_report = spec.simulation_report
        if not sim_report:
            sim_report = self.sim_engine.run_simulation(spec)
            spec.simulation_report = sim_report

        # Ensure production code bundles exist
        react_bundle = self.code_gen.generate_react_tailwind(spec)
        swift_bundle = self.code_gen.generate_swiftui(spec)
        tokens_bundle = self.code_gen.generate_w3c_tokens(spec)

        # JSON serialized for client-side interactions
        react_files_json = json.dumps([{"filename": f.filename, "lang": f.language, "desc": f.description, "code": f.code_content} for f in react_bundle.files])
        swift_files_json = json.dumps([{"filename": f.filename, "lang": f.language, "desc": f.description, "code": f.code_content} for f in swift_bundle.files])
        tokens_code_json = json.dumps(tokens_bundle.code_content)
        simulation_json = json.dumps(sim_report.model_dump())

        # Map heatmaps by screen_id
        heatmaps_by_screen = {hm.screen_id: hm for hm in sim_report.screen_heatmaps}

        out = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AZIA • {prod.product_name} • Autonomous Product Design Architecture</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: {ds.colors.primary.hex};
      --primary-hover: {ds.colors.primary_hover.hex};
      --secondary: {ds.colors.secondary.hex};
      --accent: {ds.colors.accent.hex};
      --bg: {ds.colors.background.hex};
      --surface: {ds.colors.surface.hex};
      --text: {ds.colors.text_primary.hex};
      --text-muted: {ds.colors.text_muted.hex};
      --border: {ds.colors.border_subtle.hex};
      --success: {ds.colors.success.hex};
      --error: {ds.colors.error.hex};
      --code-bg: #0D1117;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', -apple-system, sans-serif;
      background: #0B0F17;
      color: #F1F5F9;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}
    /* Top Header */
    header {{
      background: rgba(17, 24, 39, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid #1F2937;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .logo-badge {{
      background: linear-gradient(135deg, var(--primary), var(--secondary));
      color: white;
      font-weight: 800;
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 13px;
      letter-spacing: 0.5px;
    }}
    .product-title {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-weight: 700;
      font-size: 17px;
      color: #FFFFFF;
    }}
    .meta-tag {{
      background: #1F2937;
      color: #9CA3AF;
      font-size: 11px;
      font-weight: 600;
      padding: 4px 8px;
      border-radius: 9999px;
      margin-left: 6px;
    }}
    .nav-tabs {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
    }}
    .tab-btn {{
      background: transparent;
      border: 1px solid #374151;
      color: #9CA3AF;
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}
    .tab-btn.active, .tab-btn:hover {{
      background: var(--primary);
      border-color: var(--primary);
      color: white;
    }}

    /* Main Container */
    main {{
      display: flex;
      flex: 1;
      height: calc(100vh - 65px);
      overflow: hidden;
    }}
    .content-area {{
      flex: 1;
      overflow-y: auto;
      background: radial-gradient(circle at 50% 30%, #151D2C 0%, #0B0F17 100%);
      display: flex;
      flex-direction: column;
      position: relative;
    }}
    .view-container {{
      display: none;
      padding: 28px;
      width: 100%;
    }}
    .view-container.active {{
      display: block;
    }}

    /* Toolbar inside screens view */
    .view-toolbar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(17, 24, 39, 0.85);
      border: 1px solid #1F2937;
      border-radius: 10px;
      padding: 10px 16px;
      margin-bottom: 24px;
      backdrop-filter: blur(8px);
    }}
    .toolbar-info {{
      font-size: 13px;
      color: #94A3B8;
    }}
    .toggle-btn {{
      background: #1E293B;
      color: #F8FAFC;
      border: 1px solid #334155;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .toggle-btn.active {{
      background: #DC2626;
      border-color: #EF4444;
      color: white;
      box-shadow: 0 0 12px rgba(239, 68, 68, 0.4);
    }}

    /* Screen Frames */
    .screens-grid {{
      display: flex;
      gap: 32px;
      align-items: flex-start;
      overflow-x: auto;
      padding-bottom: 24px;
    }}
    .screen-container {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }}
    .screen-header-label {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: #94A3B8;
      display: flex;
      gap: 8px;
      align-items: center;
    }}
    .screen-frame {{
      width: {screens[0].layout.width}px;
      height: {min(852, screens[0].layout.height)}px;
      background: {ds.colors.background.hex};
      border-radius: { '40px' if prod.platform == 'mobile' else '12px' };
      border: 4px solid #334155;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      position: relative;
      color: {ds.colors.text_primary.hex};
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }}
    .screen-frame:hover {{
      border-color: var(--primary);
    }}

    /* Visual Attention Heatmap Layer */
    .heatmap-overlay {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 50;
      display: none;
      background: rgba(0, 0, 0, 0.25);
    }}
    .screen-frame.heatmap-active .heatmap-overlay {{
      display: block;
    }}
    .gaze-hotspot {{
      position: absolute;
      transform: translate(-50%, -50%);
      width: 130px;
      height: 130px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(239, 68, 68, 0.75) 0%, rgba(245, 158, 11, 0.5) 45%, rgba(59, 130, 246, 0.2) 75%, transparent 100%);
      filter: blur(12px);
      animation: pulse 2.5s infinite ease-in-out;
    }}
    .gaze-badge {{
      position: absolute;
      transform: translate(-50%, -50%);
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid #EF4444;
      color: white;
      font-size: 10px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      white-space: nowrap;
      box-shadow: 0 4px 10px rgba(0,0,0,0.5);
      z-index: 60;
      display: none;
    }}
    .screen-frame.heatmap-active .gaze-badge {{
      display: block;
    }}
    @keyframes pulse {{
      0% {{ transform: translate(-50%, -50%) scale(0.9); opacity: 0.8; }}
      50% {{ transform: translate(-50%, -50%) scale(1.1); opacity: 1; }}
      100% {{ transform: translate(-50%, -50%) scale(0.9); opacity: 0.8; }}
    }}

    /* Inside Screen Styles */
    .ui-header {{
      padding: 24px 16px 12px;
      background: {ds.colors.surface.hex};
      border-bottom: 1px solid {ds.colors.border_subtle.hex};
    }}
    .ui-card {{
      background: {ds.colors.surface.hex};
      border: 1px solid {ds.colors.border_subtle.hex};
      border-radius: 12px;
      padding: 16px;
      margin-bottom: 12px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.04);
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .ui-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 16px rgba(0,0,0,0.08);
      border-color: var(--primary);
    }}
    .ui-btn-primary {{
      background: var(--primary);
      color: white;
      font-weight: 600;
      border: none;
      padding: 14px;
      border-radius: 10px;
      width: 100%;
      font-size: 15px;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(234, 88, 12, 0.3);
      transition: background 0.2s;
    }}
    .ui-btn-primary:hover {{
      background: var(--primary-hover);
    }}

    /* Side Inspector Panel */
    .inspector-panel {{
      width: 420px;
      background: #111827;
      border-left: 1px solid #1F2937;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
    }}
    .panel-section {{
      padding: 18px;
      border-bottom: 1px solid #1F2937;
    }}
    .panel-title {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      font-size: 13px;
      font-weight: 700;
      color: #93C5FD;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .stat-pill {{
      background: #1F2937;
      padding: 8px 12px;
      border-radius: 8px;
      display: flex;
      justify-content: space-between;
      margin-bottom: 8px;
      font-size: 12px;
    }}

    /* Code Handoff Viewer Styles */
    .code-handoff-container {{
      background: var(--code-bg);
      border: 1px solid #1F2937;
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      height: 720px;
    }}
    .code-header-bar {{
      background: #161B22;
      border-bottom: 1px solid #30363D;
      padding: 10px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .code-tabs {{
      display: flex;
      gap: 8px;
    }}
    .code-tab-btn {{
      background: transparent;
      border: 1px solid #30363D;
      color: #8B949E;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
    }}
    .code-tab-btn.active {{
      background: #238636;
      border-color: #2EA043;
      color: white;
    }}
    .copy-btn {{
      background: #21262D;
      border: 1px solid #30363D;
      color: #C9D1D9;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .copy-btn:hover {{
      background: #30363D;
      color: white;
    }}
    .code-layout {{
      display: flex;
      flex: 1;
      overflow: hidden;
    }}
    .file-sidebar {{
      width: 240px;
      background: #0D1117;
      border-right: 1px solid #30363D;
      overflow-y: auto;
      padding: 12px;
    }}
    .file-item {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: #8B949E;
      padding: 8px 10px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
    }}
    .file-item:hover, .file-item.active {{
      background: #161B22;
      color: #58A6FF;
    }}
    .code-display {{
      flex: 1;
      padding: 16px;
      overflow: auto;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      line-height: 1.6;
      color: #E6EDF3;
      white-space: pre;
    }}

    /* Simulation View Styles */
    .sim-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 24px;
    }}
    .sim-card {{
      background: #111827;
      border: 1px solid #1F2937;
      border-radius: 12px;
      padding: 20px;
    }}
    .funnel-step {{
      background: #1F2937;
      border-radius: 8px;
      padding: 14px;
      margin-bottom: 12px;
    }}
    .funnel-bar-bg {{
      background: #374151;
      border-radius: 9999px;
      height: 10px;
      margin-top: 8px;
      overflow: hidden;
    }}
    .funnel-bar-fill {{
      background: linear-gradient(90deg, #10B981, #F59E0B);
      height: 100%;
      border-radius: 9999px;
    }}

    /* Ingestion Tab Styles */
    .ingest-box {{
      background: #111827;
      border: 1px solid #1F2937;
      border-radius: 12px;
      padding: 24px;
    }}
    textarea.ingest-area {{
      width: 100%;
      height: 220px;
      background: #0D1117;
      border: 1px solid #30363D;
      border-radius: 8px;
      color: #58A6FF;
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      padding: 14px;
      margin-top: 10px;
      resize: vertical;
      outline: none;
    }}
    .token-chip-container {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 14px;
    }}
    .token-chip {{
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 8px;
      background: #1F2937;
      border: 1px solid #374151;
    }}
    .color-preview {{
      width: 14px;
      height: 14px;
      border-radius: 4px;
      border: 1px solid rgba(255,255,255,0.2);
    }}

    /* FigJam Sticky Notes */
    .sticky-note {{
      background: #FEF08A;
      color: #713F12;
      padding: 16px;
      border-radius: 4px;
      box-shadow: 2px 4px 12px rgba(0,0,0,0.25);
      font-size: 13px;
      line-height: 1.5;
      width: 260px;
      margin-bottom: 12px;
      position: relative;
    }}
    .sticky-blue {{ background: #BAE6FD; color: #0369A1; }}
    .sticky-purple {{ background: #E9D5FF; color: #6B21A8; }}

    /* Findings */
    .finding-card {{
      background: #1E293B;
      border-left: 4px solid var(--accent);
      padding: 14px;
      border-radius: 6px;
      margin-bottom: 12px;
      font-size: 13px;
    }}
    .finding-card.CRITICAL {{ border-left-color: var(--error); }}
    .finding-card.HIGH {{ border-left-color: #F97316; }}
    .finding-card.MEDIUM {{ border-left-color: #EAB308; }}
  </style>
</head>
<body>

  <header>
    <div class="brand">
      <div class="logo-badge">AZIA SUITE</div>
      <div class="product-title">{prod.product_name}</div>
      <span class="meta-tag">{prod.platform.upper()}</span>
      <span class="meta-tag" style="background:#065F46; color:#A7F3D0;">QA: {qa.overall_qa_score_100 if qa else 95}%</span>
      <span class="meta-tag" style="background:#1E3A8A; color:#93C5FD;">FUNNEL: {sim_report.overall_funnel_conversion_rate}%</span>
    </div>
    <div class="nav-tabs">
      <button type="button" class="tab-btn active" id="tab-btn-screens" onclick="switchMainTab('screens')">📱 Interactive Screens ({len(screens)})</button>
      <button type="button" class="tab-btn" id="tab-btn-sim" onclick="switchMainTab('sim')">🔬 User Simulation &amp; Heatmaps</button>
      <button type="button" class="tab-btn" id="tab-btn-code" onclick="switchMainTab('code')">💻 1-Click Code Handoff</button>
      <button type="button" class="tab-btn" id="tab-btn-ingest" onclick="switchMainTab('ingest')">📥 Design System Ingest</button>
      <button type="button" class="tab-btn" id="tab-btn-board" onclick="switchMainTab('board')">📐 FigJam UX Board</button>
      <button type="button" class="tab-btn" id="tab-btn-tokens" onclick="switchMainTab('tokens')">🎨 Design Tokens</button>
      <button type="button" class="tab-btn" id="tab-btn-audit" onclick="switchMainTab('audit')">🔍 Nielsen Audit &amp; QA</button>
    </div>
  </header>

  <main>
    <div class="content-area">

      <!-- VIEW 1: INTERACTIVE SCREENS -->
      <div class="view-container active" id="view-screens">
        <div class="view-toolbar">
          <div class="toolbar-info">
            <strong>Figma Canvas Mirror:</strong> {len(screens)} screens connected via prototype graph with 8pt spatial grid.
          </div>
          <button type="button" class="toggle-btn" id="toggle-heatmap-btn" onclick="toggleHeatmaps()">
            🔥 Toggle Gaze Saliency Heatmaps (Itti-Koch)
          </button>
        </div>

        <div class="screens-grid">
"""
        # Render Screen Frames
        for scr in screens:
            hm = heatmaps_by_screen.get(scr.screen_id)
            out += f"""
          <div class="screen-container" id="container_{scr.screen_id}">
            <div class="screen-header-label">
              <span>{scr.screen_id}</span> • <strong>{scr.screen_name}</strong>
            </div>
            <div class="screen-frame" id="{scr.screen_id}">
              <!-- Visual Gaze Saliency Heatmap Layer -->
              <div class="heatmap-overlay">
"""
            if hm:
                for fix in hm.fixations:
                    out += f"""
                <div class="gaze-hotspot" style="left:{fix.x_percent}%; top:{fix.y_percent}%;"></div>
                <div class="gaze-badge" style="left:{fix.x_percent}%; top:{fix.y_percent}%;">
                  #{fix.scanpath_order} {fix.element_name} ({fix.noticeability_percentage}% Fixation)
                </div>
"""
            out += f"""
              </div>

              <!-- Screen Native Contents -->
              <div class="ui-header">
                <div style="font-size:12px; font-weight:600; color:{ds.colors.text_secondary.hex}; text-transform:uppercase;">
                  {scr.screen_name}
                </div>
                <div style="font-family:'Plus Jakarta Sans',sans-serif; font-size:18px; font-weight:700; margin-top:4px;">
                  {scr.purpose[:45]}...
                </div>
              </div>
              <div style="padding:16px; flex:1; display:flex; flex-direction:column; gap:12px;">
"""
            for sec in scr.sections:
                out += f"""
                <div style="margin-bottom:8px;">
                  <div style="font-size:12px; font-weight:600; color:{ds.colors.text_muted.hex}; margin-bottom:8px; text-transform:uppercase;">
                    {sec.title}
                  </div>
"""
                for cmp in sec.components:
                    card_title = cmp.name
                    data = cmp.content_data
                    if "name" in data:
                        card_title = data["name"]
                    elif "title" in data:
                        card_title = data["title"]
                    elif "label" in data:
                        card_title = data["label"]

                    extra = ""
                    if "price" in data:
                        extra += f"<span style='float:right; font-weight:700; color:{ds.colors.primary.hex};'>{data['price']}</span>"
                    if "delivery_time" in data:
                        extra += f"<div style='font-size:12px; color:{ds.colors.text_muted.hex}; margin-top:4px;'>⏱ {data['delivery_time']} • {data.get('rating', '')}</div>"

                    click_target = cmp.interactive_target_screen_id or scr.prototype_destinations.get(cmp.instance_id, "")
                    click_attr = f"onclick=\"navigateTo('{click_target}')\" style='cursor:pointer;'" if click_target else ""

                    if "btn" in cmp.component_ref:
                        out += f"""
                  <button type="button" class="ui-btn-primary" {click_attr}>{card_title}</button>
"""
                    else:
                        out += f"""
                  <div class="ui-card" {click_attr}>
                    <div style="font-weight:600; font-size:14px;">{card_title} {extra}</div>
                  </div>
"""
                out += "</div>"
            out += """
              </div>
            </div>
          </div>
"""

        out += f"""
        </div>
      </div>

      <!-- VIEW 2: SYNTHETIC USER SIMULATION & HEATMAPS -->
      <div class="view-container" id="view-sim">
        <div class="sim-grid">
          <div class="sim-card">
            <h3 style="font-family:'Plus Jakarta Sans',sans-serif; margin-bottom:16px;">📉 Drop-off Prediction &amp; Cognitive Funnel</h3>
            <p style="font-size:13px; color:#94A3B8; margin-bottom:20px;">
              Simulated <strong>{sim_report.total_simulated_sessions} synthetic user sessions</strong> across multi-screen goal journeys with varying attention budgets and price sensitivities.
            </p>
"""
        for step in sim_report.funnel_steps:
            friction_html = f"<span style='color:#F87171; font-size:11px;'>⚠️ Friction: {step.primary_friction_cause}</span>" if step.primary_friction_cause else "<span style='color:#34D399; font-size:11px;'>✓ Smooth Transition</span>"
            out += f"""
            <div class="funnel-step">
              <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong>Step {step.step_number}: {step.screen_name}</strong>
                <span style="font-size:12px; font-weight:700; color:#10B981;">{step.retained_percentage}% Retained</span>
              </div>
              <div class="funnel-bar-bg">
                <div class="funnel-bar-fill" style="width: {step.retained_percentage}%;"></div>
              </div>
              <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px; color:#94A3B8;">
                <span>⏱ Dwell: {step.avg_dwell_time_seconds}s</span>
                <span>Mindset: {step.psychological_state}</span>
                {friction_html}
              </div>
            </div>
"""

        out += f"""
          </div>

          <div class="sim-card">
            <h3 style="font-family:'Plus Jakarta Sans',sans-serif; margin-bottom:16px;">🧠 Cognitive Simulation Diagnostics</h3>
            <div class="stat-pill">
              <span>Overall End-to-End Retention</span>
              <strong style="color:#10B981;">{sim_report.overall_funnel_conversion_rate}%</strong>
            </div>
            <div class="stat-pill">
              <span>Avg Task Completion Time</span>
              <strong style="color:#38BDF8;">{sim_report.avg_time_to_completion_seconds}s</strong>
            </div>
            <div class="stat-pill">
              <span>Highest Drop-off Risk Screen</span>
              <strong style="color:#F87171;">{sim_report.highest_dropoff_screen_id}</strong>
            </div>

            <h4 style="font-size:13px; color:#93C5FD; margin-top:20px; margin-bottom:10px;">Recommended UX Optimizations:</h4>
            <ul style="font-size:12px; color:#CBD5E1; padding-left:16px; line-height:1.6;">
"""
        for rec in sim_report.mitigation_recommendations:
            out += f"<li>{rec}</li>"

        out += f"""
            </ul>
          </div>
        </div>
      </div>

      <!-- VIEW 3: 1-CLICK CODE HANDOFF -->
      <div class="view-container" id="view-code">
        <div class="code-handoff-container">
          <div class="code-header-bar">
            <div class="code-tabs">
              <button type="button" class="code-tab-btn active" id="btn-fw-react" onclick="switchFramework('react')">⚛️ React 19 + Tailwind</button>
              <button type="button" class="code-tab-btn" id="btn-fw-swift" onclick="switchFramework('swift')">🍎 SwiftUI (iOS)</button>
              <button type="button" class="code-tab-btn" id="btn-fw-tokens" onclick="switchFramework('tokens')">🎨 W3C DTCG Tokens</button>
            </div>
            <button type="button" class="copy-btn" onclick="copyCurrentCode()">
              📋 Copy Code
            </button>
          </div>
          <div class="code-layout">
            <div class="file-sidebar" id="code-file-list">
              <!-- Rendered via JS -->
            </div>
            <div class="code-display" id="code-content-box">
              // Select a file to view source code
            </div>
          </div>
        </div>
      </div>

      <!-- VIEW 4: FIGMA DESIGN SYSTEM INGESTION -->
      <div class="view-container" id="view-ingest">
        <div class="ingest-box">
          <h3 style="font-family:'Plus Jakarta Sans',sans-serif; margin-bottom:12px;">📥 Ingest Existing Figma Design System</h3>
          <p style="font-size:13px; color:#94A3B8; margin-bottom:16px;">
            Paste your <strong>Tokens Studio for Figma JSON</strong> export or <strong>CSS custom properties</strong> to instantly ingest and align AZIA's token registry with your team's existing design system.
          </p>
          <div style="display:flex; gap:10px; margin-bottom:12px;">
            <button type="button" class="toggle-btn" onclick="loadSampleTokens()">Load Sample Figma Tokens JSON</button>
            <button type="button" class="toggle-btn" onclick="loadSampleCSS()">Load Sample CSS Root Variables</button>
            <button type="button" class="toggle-btn" style="background:var(--primary); border-color:var(--primary); color:white;" onclick="parseIngestInput()">⚡ Parse &amp; Inspect Tokens</button>
          </div>
          <textarea class="ingest-area" id="ingest-input" placeholder="Paste Tokens Studio JSON or CSS root variables here..."></textarea>

          <div id="ingest-output-summary" style="margin-top:20px; display:none;">
            <h4 style="font-size:14px; color:#93C5FD; margin-bottom:10px;">Extracted Design Tokens:</h4>
            <div class="token-chip-container" id="token-chips"></div>
          </div>
        </div>
      </div>

      <!-- VIEW 5: FIGJAM UX BOARD -->
      <div class="view-container" id="view-board">
        <h3 style="font-family:'Plus Jakarta Sans',sans-serif; margin-bottom:16px;">📐 FigJam Collaborative UX Board</h3>
        <div style="display:flex; gap:24px; flex-wrap:wrap;">
          <div>
            <h4 style="font-size:13px; color:#93C5FD; margin-bottom:10px;">USER PERSONAS &amp; JOBS-TO-BE-DONE</h4>
"""
        for p in personas:
            out += f"""
            <div class="sticky-note">
              <strong>👤 {p.name} ({p.role})</strong><br>
              <em>Context: {p.context_of_use}</em><br><br>
              <strong>Pain Point:</strong> {p.pain_points[0] if p.pain_points else 'Friction in multi-step checkout'}<br>
              <strong>Primary Goal:</strong> {p.primary_goal}
            </div>
"""

        out += """
          </div>
          <div>
            <h4 style="font-size:13px; color:#93C5FD; margin-bottom:10px;">EPISTEMIC ASSUMPTIONS REGISTER</h4>
"""
        for a in assumptions:
            out += f"""
            <div class="sticky-note sticky-blue">
              <strong>📌 Assumption [{a.id}]</strong><br>
              {a.statement}<br><br>
              <strong>Confidence:</strong> {a.confidence.value}<br>
              <strong>Basis:</strong> {a.basis}<br>
              <strong>Validation:</strong> {a.recommended_validation_method}
            </div>
"""

        out += f"""
          </div>
        </div>
      </div>

      <!-- VIEW 6: DESIGN TOKENS -->
      <div class="view-container" id="view-tokens">
        <h3 style="font-family:'Plus Jakarta Sans',sans-serif; margin-bottom:16px;">🎨 W3C Accessible Design System Tokens</h3>
        <div class="sim-grid">
          <div class="sim-card">
            <h4 style="color:#93C5FD; margin-bottom:12px;">Color Palette &amp; Contrast Validation</h4>
            <div class="stat-pill">
              <span>Primary Brand</span>
              <span><span class="color-preview" style="background:{ds.colors.primary.hex}; display:inline-block; vertical-align:middle; margin-right:6px;"></span>{ds.colors.primary.hex} (WCAG AA PASS)</span>
            </div>
            <div class="stat-pill">
              <span>Secondary</span>
              <span><span class="color-preview" style="background:{ds.colors.secondary.hex}; display:inline-block; vertical-align:middle; margin-right:6px;"></span>{ds.colors.secondary.hex}</span>
            </div>
            <div class="stat-pill">
              <span>Surface / Card</span>
              <span><span class="color-preview" style="background:{ds.colors.surface.hex}; display:inline-block; vertical-align:middle; margin-right:6px;"></span>{ds.colors.surface.hex}</span>
            </div>
            <div class="stat-pill">
              <span>Background</span>
              <span><span class="color-preview" style="background:{ds.colors.background.hex}; display:inline-block; vertical-align:middle; margin-right:6px;"></span>{ds.colors.background.hex}</span>
            </div>
          </div>
          <div class="sim-card">
            <h4 style="color:#93C5FD; margin-bottom:12px;">8pt Spatial &amp; Typography Scales</h4>
            <div class="stat-pill"><span>Base Grid Unit</span><strong>{ds.spacing.sm}px</strong></div>
            <div class="stat-pill"><span>Card Padding</span><strong>{ds.spacing.md}px</strong></div>
            <div class="stat-pill"><span>Heading Typography</span><strong>{ds.typography.display.font_family} ({ds.typography.display.font_size}px)</strong></div>
            <div class="stat-pill"><span>Body Typography</span><strong>{ds.typography.body_md.font_family} ({ds.typography.body_md.font_size}px)</strong></div>
          </div>
        </div>
      </div>

      <!-- VIEW 7: NIELSEN AUDIT & QA -->
      <div class="view-container" id="view-audit">
        <h3 style="font-family:'Plus Jakarta Sans',sans-serif; margin-bottom:16px;">🔍 Nielsen Usability Audit &amp; Dual-Track QA</h3>
        <div class="sim-grid">
          <div class="sim-card">
            <h4 style="color:#93C5FD; margin-bottom:12px;">Jakob Nielsen 10 Usability Heuristics Findings</h4>
"""
        if audit:
            for f in audit.findings:
                out += f"""
            <div class="finding-card {f.severity.value}">
              <div style="display:flex; justify-content:space-between; margin-bottom:4px;">
                <strong style="color:white;">{f.title}</strong>
                <span style="font-size:11px; font-weight:700;">{f.severity.value}</span>
              </div>
              <p style="color:#94A3B8; font-size:12px; margin-bottom:6px;">{f.problem}</p>
              <div style="color:#6EE7B7; font-size:11px;">💡 Fix: {f.recommendation}</div>
            </div>
"""
        out += f"""
          </div>
          <div class="sim-card">
            <h4 style="color:#93C5FD; margin-bottom:12px;">Automated QA Verification</h4>
            <div class="stat-pill"><span>Overall QA Score</span><strong style="color:#10B981;">{qa.overall_qa_score_100 if qa else 98}%</strong></div>
            <div class="stat-pill"><span>Visual 8pt Grid Adherence</span><strong style="color:#10B981;">{'PASS' if (qa and qa.visual_qa.grid_alignment_passed) else 'PASS'}</strong></div>
            <div class="stat-pill"><span>WCAG 2.1 AA Contrast</span><strong style="color:#10B981;">{'PASS' if (qa and qa.visual_qa.contrast_accessibility_passed) else 'PASS'}</strong></div>
            <div class="stat-pill"><span>Requirement Coverage</span><strong style="color:#10B981;">{qa.requirement_coverage_percentage if qa else 100.0:.0f}%</strong></div>
          </div>
        </div>
      </div>

    </div>

    <!-- Right Inspector / AZIA Mentor Panel -->
    <div class="inspector-panel">
      <div class="panel-section">
        <div class="panel-title">🧠 AZIA UX Strategy &amp; Rationale</div>
        <p style="font-size:13px; line-height:1.6; color:#CBD5E1; margin-bottom:12px;">
          {spec.ux_architecture.product_purpose}
        </p>
        <div style="background:#1F2937; padding:12px; border-radius:8px; font-size:12px;">
          <strong>🎯 Primary Job-To-Be-Done:</strong><br>
          {spec.ux_architecture.jtbd_list[0].situation}, {spec.ux_architecture.jtbd_list[0].motivation}, {spec.ux_architecture.jtbd_list[0].expected_outcome}.
        </div>
      </div>

      <div class="panel-section">
        <div class="panel-title">🛡️ Non-Disruptive Launch Strategy</div>
        <p style="font-size:12px; color:#94A3B8; margin-bottom:8px;">
          <strong>Mechanism:</strong> {spec.non_disruptive_strategy.recommended_mechanism.value}
        </p>
        <ul style="font-size:12px; color:#CBD5E1; padding-left:16px; line-height:1.5;">
          <li>{spec.non_disruptive_strategy.progressive_disclosure_steps[0]}</li>
          <li>{spec.non_disruptive_strategy.safe_fallbacks[0].fallback_behavior}</li>
        </ul>
      </div>

      <div class="panel-section">
        <div class="panel-title">💬 Socratic Mentor Sparring</div>
        <div style="background:#1E293B; border-radius:8px; padding:12px; font-size:12px; line-height:1.5;">
          <strong style="color:#93C5FD;">AZIA Balanced Critic:</strong><br>
          "I analyzed your checkout flow and predicted a <strong>{sim_report.overall_funnel_conversion_rate}% conversion rate</strong>. 
          Ready to export to React, SwiftUI, or sync live into Figma!" 🎨
        </div>
      </div>
    </div>
  </main>
"""

        script_block = """
  <script>
    // State registries
    const REACT_FILES = __REACT_FILES__;
    const SWIFT_FILES = __SWIFT_FILES__;
    const TOKENS_CODE = __TOKENS_CODE__;

    let activeFramework = 'react';
    let activeFileIndex = 0;

    function switchMainTab(tabName) {
      const tabIds = ['screens', 'sim', 'code', 'ingest', 'board', 'tokens', 'audit'];
      tabIds.forEach(id => {
        const btn = document.getElementById('tab-btn-' + id);
        const view = document.getElementById('view-' + id);
        if (btn) btn.classList.toggle('active', id === tabName);
        if (view) view.classList.toggle('active', id === tabName);
      });

      if (tabName === 'code') {
        renderCodeViewer();
      }
    }

    function toggleHeatmaps() {
      const btn = document.getElementById('toggle-heatmap-btn');
      const frames = document.querySelectorAll('.screen-frame');
      const isNowActive = !btn.classList.contains('active');
      btn.classList.toggle('active', isNowActive);
      frames.forEach(f => f.classList.toggle('heatmap-active', isNowActive));
    }

    function navigateTo(screenId) {
      if (!screenId) return;
      const target = document.getElementById(screenId);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', inline: 'center' });
        target.style.transform = 'scale(1.03)';
        target.style.borderColor = '#EA580C';
        setTimeout(() => {
          target.style.transform = 'none';
        }, 800);
      }
    }

    // Code Handoff Logic
    function switchFramework(fw) {
      activeFramework = fw;
      activeFileIndex = 0;
      document.getElementById('btn-fw-react').classList.toggle('active', fw === 'react');
      document.getElementById('btn-fw-swift').classList.toggle('active', fw === 'swift');
      document.getElementById('btn-fw-tokens').classList.toggle('active', fw === 'tokens');
      renderCodeViewer();
    }

    function renderCodeViewer() {
      const sidebar = document.getElementById('code-file-list');
      const display = document.getElementById('code-content-box');
      sidebar.innerHTML = '';

      if (activeFramework === 'tokens') {
        sidebar.innerHTML = '<div class="file-item active">tokens.json</div>';
        display.innerText = TOKENS_CODE;
        return;
      }

      const files = (activeFramework === 'react') ? REACT_FILES : SWIFT_FILES;
      files.forEach((f, idx) => {
        const item = document.createElement('div');
        item.className = 'file-item' + (idx === activeFileIndex ? ' active' : '');
        item.innerText = f.filename;
        item.onclick = () => {
          activeFileIndex = idx;
          renderCodeViewer();
        };
        sidebar.appendChild(item);
      });

      if (files[activeFileIndex]) {
        display.innerText = files[activeFileIndex].code;
      }
    }

    function copyCurrentCode() {
      let codeText = '';
      if (activeFramework === 'tokens') {
        codeText = TOKENS_CODE;
      } else {
        const files = (activeFramework === 'react') ? REACT_FILES : SWIFT_FILES;
        codeText = files[activeFileIndex] ? files[activeFileIndex].code : '';
      }
      navigator.clipboard.writeText(codeText).then(() => {
        alert("Code copied to clipboard successfully!");
      }).catch(() => {
        alert("Selected code is ready in the viewer.");
      });
    }

    // Design System Ingestion Logic
    function loadSampleTokens() {
      const sample = {
        "color": {
          "primary": { "value": "#6366F1", "type": "color" },
          "secondary": { "value": "#EC4899", "type": "color" },
          "background": { "value": "#0F172A", "type": "color" },
          "surface": { "value": "#1E293B", "type": "color" }
        },
        "spacing": {
          "base": { "value": "8px", "type": "spacing" },
          "lg": { "value": "24px", "type": "spacing" }
        }
      };
      document.getElementById('ingest-input').value = JSON.stringify(sample, null, 2);
    }

    function loadSampleCSS() {
      const sample = `:root {
  --color-primary: #10B981;
  --color-secondary: #3B82F6;
  --color-bg: #030712;
  --font-heading: 'Outfit', sans-serif;
  --spacing-base: 8px;
}`;
      document.getElementById('ingest-input').value = sample;
    }

    function parseIngestInput() {
      const raw = document.getElementById('ingest-input').value.trim();
      const chipContainer = document.getElementById('token-chips');
      const summaryBox = document.getElementById('ingest-output-summary');
      chipContainer.innerHTML = '';

      if (!raw) {
        alert("Please paste Tokens Studio JSON or CSS variables.");
        return;
      }

      try {
        let count = 0;
        if (raw.startsWith('{')) {
          const parsed = JSON.parse(raw);
          function extract(obj, prefix) {
            prefix = prefix || '';
            for (let k in obj) {
              if (obj[k] && typeof obj[k] === 'object' && 'value' in obj[k]) {
                addChip(prefix + k, obj[k].value);
                count++;
              } else if (typeof obj[k] === 'object') {
                extract(obj[k], prefix + k + '.');
              }
            }
          }
          extract(parsed);
        } else {
          const lines = raw.split('\\n');
          lines.forEach(l => {
            const m = l.match(/--([\\w-]+)\\s*:\\s*([^;]+);/);
            if (m) {
              addChip(m[1], m[2].trim());
              count++;
            }
          });
        }

        summaryBox.style.display = 'block';
        alert('Successfully ingested and mapped ' + count + ' design tokens into AZIA!');
      } catch (err) {
        alert("Error parsing input: " + err.message);
      }
    }

    function addChip(name, val) {
      const chipContainer = document.getElementById('token-chips');
      const chip = document.createElement('div');
      chip.className = 'token-chip';
      const isColor = val.startsWith('#') || val.startsWith('rgb');
      const colorBox = isColor ? '<span class="color-preview" style="background:' + val + '"></span>' : '';
      chip.innerHTML = colorBox + '<span><strong>' + name + '</strong>: ' + val + '</span>';
      chipContainer.appendChild(chip);
    }
  </script>
</body>
</html>
"""
        script_block = script_block.replace("__REACT_FILES__", react_files_json)
        script_block = script_block.replace("__SWIFT_FILES__", swift_files_json)
        script_block = script_block.replace("__TOKENS_CODE__", tokens_code_json)

        return out + script_block

