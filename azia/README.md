# AZIA • Autonomous AI Product Design Engineer & Figma MCP

> **One Requirement. One Command. Complete Product Design.**  
> *Not a mockup. Not a tutorial. Not a conversational chatbot. An autonomous design engineering system.*

---

## 🌟 What is AZIA?
**AZIA** is an autonomous AI product design engineer, UX architect, design system engineer, and Figma plugin execution engine packaged with standard **Model Context Protocol (MCP)** support.

Given a high-level natural language prompt such as:
> *"Build a modern food delivery app for college students. Students should discover nearby restaurants, search food, order food, pay, and track delivery."*

AZIA autonomously reasons through the entire UX/UI lifecycle without requiring manual screen-by-screen prompting:
1. **Pre-Flight Ambiguity Inspection:** Evaluates context sufficiency and asks targeted clarification questions before blind generation.
2. **Requirement Intelligence & Epistemic Taxonomy:** Extracts entities, actions, and constraints, strictly classifying knowledge into `CONFIRMED`, `INFERRED`, `ASSUMPTION`, and `UNKNOWN`.
3. **Evidence-Grounded UX Architecture:** Derives behavioral User Personas and Jobs-to-be-Done (JTBD).
4. **Information Architecture (IA):** Determines navigation paradigms (bottom tabs, sidebars) and screen grouping hierarchies.
5. **Graph-Based User Flows:** Synthesizes topological flows with automated dead-end and error recovery validation.
6. **Accessible Design System:** Generates mathematical 8pt spatial grid scales, typographic hierarchies, and WCAG 2.1 AA/AAA contrast-verified color tokens.
7. **Semantic Component Registry:** Plans 30+ reusable atomic components with Auto Layout parameters and variant states.
8. **Screen Planning & Realistic Content:** Constructs multi-section screens using Auto Layout with domain-accurate copy (zero *"Lorem Ipsum"*).
9. **Interactive Prototyping:** Connects click affordances to destination screens with realistic transition animations.
10. **Non-Disruptive Launch Strategy:** Formulates progressive disclosure ladders, opt-in feature toggles, and safe fallback workflows.
11. **Jakob Nielsen 10 Usability Heuristics Audit:** Conducts automated heuristic inspections with structured severity findings and actionable fixes.
12. **Dual-Track Visual & Requirement QA:** Mathematically audits 8pt grid alignment, typographic contrast, component reuse ratios, and 100% requirement coverage.
13. **Bounded Autonomous Self-Repair:** Executes an automated `Inspect -> Fix -> Verify` repair loop (bounded to 3 iterations).
14. **Deterministic Figma Plugin Sandbox:** Emits strictly-typed semantic operations tagged with `managed_by="autonomous-design-mcp"` ensuring non-destructive execution on live Figma/FigJam canvases.

---

## 📁 Repository Structure (Self-Contained in `azia/`)
```
azia/
├── README.md                           # Master documentation
├── requirements.txt                    # Python dependencies
├── package.json                        # Node/Figma plugin package manifest
├── run_azia.py                         # Master CLI direct execution runner
├── mcp_server.py                       # MCP Server exposing design_product, spar, audit
├── azia_core/                          # Core Python package
│   ├── models/                         # Pydantic domain models
│   │   ├── taxonomy.py                 # Epistemic register, evidence, assumptions
│   │   ├── preflight.py                # Ambiguity checks & clarification questions
│   │   ├── ux_artifacts.py             # Personas, JTBD, user journeys
│   │   ├── ia.py                       # Navigation models & screen grouping
│   │   ├── flows.py                    # Graph nodes, transitions, flow health
│   │   ├── design_system.py            # Tokens, 8pt grid, WCAG AA/AAA colors
│   │   ├── components.py               # 30+ semantic component definitions
│   │   ├── screens.py                  # Screen layouts, sections, component binds
│   │   ├── prototype.py                # Prototype triggers, connections, animations
│   │   ├── strategy.py                 # Progressive disclosure & safe fallbacks
│   │   ├── audit.py                    # Nielsen 10 heuristics & accessibility
│   │   ├── qa.py                       # Visual QA checks & requirement coverage
│   │   ├── specification.py            # Unified ProductDesignSpecification schema
│   │   └── operations.py               # Semantic Figma operations protocol
│   ├── intelligence/                   # Cognitive AI reasoning engines
│   │   ├── preflight_engine.py         # Ambiguity detection
│   │   ├── requirement_engine.py       # Entity & constraint extraction
│   │   ├── ux_engine.py                # Persona & JTBD synthesizer
│   │   ├── ia_engine.py                # Information architect
│   │   ├── flow_engine.py              # Journey & state planner
│   │   ├── design_system_engine.py     # Token & color palette generator
│   │   ├── component_engine.py         # Reusable component architect
│   │   ├── screen_engine.py            # Layout & Auto Layout planner
│   │   ├── content_engine.py           # Domain realistic copy generator
│   │   ├── prototype_engine.py         # Interaction graph synthesizer
│   │   ├── strategy_engine.py          # Non-disruptive launch planner
│   │   ├── mentor_sparring.py          # AZIA Socratic mentor & balanced critic
│   │   ├── audit_engine.py             # Nielsen 10 Heuristics auditor
│   │   ├── qa_engine.py                # Dual-track QA inspector
│   │   └── repair_engine.py            # Bounded self-repair optimization loop
│   ├── renderer/                       # Deterministic Figma Renderer
│   │   ├── operation_planner.py        # Maps specs into ordered semantic operations
│   │   ├── virtual_canvas.py           # Virtual Figma DOM engine & scene graph
│   │   ├── visual_exporter.py          # Standalone interactive HTML/SVG preview
│   │   └── figma_exporter.py           # Figma Plugin JSON payload generator
│   └── orchestrator.py                 # Autonomous Master Pipeline Orchestrator
├── plugin/                             # Real Figma & FigJam Plugin
│   ├── manifest.json                   # Figma Plugin manifest
│   ├── src/code.ts                     # TypeScript sandbox engine
│   ├── dist/code.js                    # Compiled sandbox bundle
│   └── src/ui.html                     # Rich interactive plugin interface
├── tests/                              # Pytest automated test suite (13/13 passing)
│   ├── test_requirement_engine.py
│   ├── test_ux_ia_flow.py
│   ├── test_design_system_and_screens.py
│   ├── test_renderer_operations.py
│   ├── test_qa_and_repair.py
│   └── test_end_to_end_domains.py      # E2E tests for Food Delivery & SaaS PM
├── output/                             # Direct generated results!
│   ├── food_delivery/                  # Food Delivery Mobile App Artifacts
│   │   ├── design_specification.json   # 79 KB complete specification
│   │   ├── figma_operations.json       # 80 deterministic Figma operations
│   │   ├── preview.html                # Interactive visual prototype preview
│   │   ├── ux_reasoning_report.md      # Comprehensive UX architecture report
│   │   └── qa_audit_report.json        # QA & Nielsen audit findings
│   └── saas_pm/                        # Developer Project Management SaaS Artifacts
│       ├── design_specification.json   # 60 KB complete specification
│       ├── figma_operations.json       # 47 deterministic Figma operations
│       ├── preview.html                # Interactive visual prototype preview
│       ├── ux_reasoning_report.md      # Comprehensive UX architecture report
│       └── qa_audit_report.json        # QA & Nielsen audit findings
└── docs/
    ├── ARCHITECTURE.md                 # Deep technical architecture
    ├── UX_REASONING_MANIFESTO.md       # Complete UX designer reasoning manifesto
    └── FIGMA_PLUGIN_GUIDE.md           # Step-by-step Figma setup instructions
```

---

## ⚡ Direct Results Generated
Direct results for both mandatory end-to-end domains have been generated and validated:

### 1. Campus Food Delivery Mobile App (`CraveBite Campus`)
- **Location:** `azia/output/food_delivery/`
- **Screens Generated (7):**
  1. `scr_home`: Campus Discovery & Flash Student Deals Feed
  2. `scr_search`: Dietary Search & Budget Filter Results
  3. `scr_restaurant_detail`: Menu Customizer with Portion & Add-on Selectors
  4. `scr_cart`: Cart Review with Dorm Landmark Drop Point
  5. `scr_checkout`: Frictionless 1-Tap Payment Authorization (Apple Pay & Student Cash)
  6. `scr_order_confirmation`: Kitchen Ticket Status & Prep Timer
  7. `scr_order_tracking`: Live Campus Courier GPS Map with 4-Digit Pickup PIN
- **Master Components (12):** Buttons, Search Bar, Entity Cards, Dietary Badges, Floating Cart Bar, Modals.
- **Figma Operations (80):** Strict Auto Layout specifications ready to render into Figma.
- **QA Score:** 100% (100% Requirement Coverage).
- **Usability Score:** 88/100 (Audited against Nielsen Heuristics).

### 2. Engineering Project Management SaaS (`SprintFlow Workspace`)
- **Location:** `azia/output/saas_pm/`
- **Screens Generated (4):**
  1. `scr_dashboard`: Sprint Burndown KPI Dashboard & Blocker Alerts
  2. `scr_kanban_board`: 5-Column Agile Sprint Board (Backlog, Dev, Review, Done)
  3. `scr_task_detail`: Task Specification & GitHub PR Traceability Drawer
  4. `scr_analytics`: Sprint Velocity, Cycle Time & Burndown Analytics
- **Master Components (13):** Global Sidebar Navigation, Kanban Columns, Priority Badges, Task Cards, Data Tables.
- **Figma Operations (47):** Strict Auto Layout operations.
- **QA Score:** 100% (100% Requirement Coverage).
- **Usability Score:** 88/100.

---

## 🚀 Running AZIA

### Run via Master CLI:
```bash
# Generate Food Delivery Product Design
python azia/run_azia.py --requirement "Build a modern food delivery app for college students. Students should discover nearby restaurants, search food, order food, pay, and track delivery." --output-dir azia/output/food_delivery --platform mobile

# Generate SaaS Project Management Product Design
python azia/run_azia.py --requirement "Build a project management SaaS for small engineering teams. Teams should create projects, manage tasks, assign work, track progress, and see project status." --output-dir azia/output/saas_pm --platform desktop
```

### Run Automated Pytest Suite:
```bash
python -m pytest azia/tests -v
```
*(All 13 unit, integration, and cross-domain E2E tests pass in under 1 second)*

### Run MCP Server:
```bash
python azia/mcp_server.py
```
Exposes:
- `design_product(requirement, platform, style, fidelity)`
- `preflight_check(requirement)`
- `spar_with_agent(query)`
- `run_design_qa(generation_id)`
- `rollback_generation(generation_id)`

---

## 🎨 Viewing the Interactive Previews
Open either preview directly in any web browser:
- `azia/output/food_delivery/preview.html`
- `azia/output/saas_pm/preview.html`

Features:
- Live mobile / desktop frame simulation
- Clickable prototype flows that smoothly scroll and highlight destination screens
- UX Architecture Inspector with Personas and Jobs-to-be-Done
- Non-Disruptive Launch Strategy breakdown
- Nielsen 10 Usability Heuristics Audit findings with severity indicators
- AZIA Socratic Mentor sparring panel.
