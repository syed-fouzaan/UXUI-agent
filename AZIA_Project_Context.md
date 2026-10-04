# AZIA • AI UX Mentor & Autonomous Design MCP
## Master Project Context, Architectural Specification & System Manifesto

> **"AZIA does not design for you. It helps you make better design decisions."**  
> **"AZIA should not make designers feel replaced. It should make them think better."**  
> — *Core AZIA Product Mantras*

---

## 1. Executive Summary & Current Project Status

**AZIA** is an autonomous, evidence-aware AI UX design agent and Socratic sparring mentor built for product designers, design engineers, and UX researchers. Unlike traditional generative AI tools that simply output generic landing pages or hallucinated wireframes without rationale, AZIA reasons deeply about user journeys, information architecture, cognitive load, accessibility (WCAG 2.1 AA/AAA), design systems, and multi-state edge cases before synthesizing production-grade UI and deterministic Figma canvas operations.

### Current Implementation Status (Active & Deployed)
AZIA has evolved from an initial concept into a fully implemented, cloud-deployed, and automated design system with a 100% passing test suite (28/28 pytest tests):

| Component | Status | Location / URL | Description |
| :--- | :--- | :--- | :--- |
| **Cloud Backend API** | **Live Production** | `https://uxui-agent.onrender.com` | FastAPI autonomous UX engine with REST endpoints, CORS preflight, and dynamic key configuration. |
| **Web Design Studio** | **Live Production** | `https://uxui-agent.onrender.com` | Glassmorphic dark workspace for prompt input, real-time telemetry, Socratic chat, and instant payload copying. |
| **Figma Plugin** | **Installed & Connected** | `azia/plugin/` & `/download-plugin` | Dual-mode plugin with offline instant demo architectures, live Render cloud generation, Nielsen audit, and Socratic sparring. |
| **AI LLM Orchestration** | **Multi-Provider Active** | `azia/llm_client.py` | Google Gemini 3.8 Flash + xAI Grok + offline heuristic fallback engine. |
| **Deterministic Figma Engine** | **Verified** | `azia/plugin/dist/code.js` | Ingests JSON ops and renders auto-layout frames, color tokens, typography, rich cards, buttons, badges, and prototyping wires. |
| **Automated Test Suite** | **28/28 Passing** | `azia/tests/` | 100% coverage across requirements, IA, tokens, screens, simulation, self-repair loop, and MCP server. |

---

## 2. Core Product Vision & Positioning

### The Market Problem
Most AI design tools focus exclusively on surface-level visual generation:
- Generating isolated, non-functional screens
- Rewriting placeholder text into marketing copy
- Hallucinating components disconnected from design tokens
- Producing "happy-path" mockups that collapse under real-world edge cases

### The AZIA Differentiation: UX Intelligence
AZIA sits in a fundamentally different category:
```
Traditional AI:  Prompt ─────────────► Hallucinated UI Mockup
AZIA Loop:       Understand ──► Research ──► Challenge ──► Evaluate ──► Decide ──► Synthesize ──► Document ──► Validate
```

AZIA behaves like a **Senior Staff Product Designer and Design Mentor sitting beside you**:
1. **Explainable**: Every decision cites established cognitive psychology or UX principles (Nielsen Norman Group, Fitts's Law, Miller's Law, Hicks's Law, Progressive Disclosure).
2. **Evidence-Aware**: Clearly differentiates between empirical facts, research insights, assumptions, and AI hypotheses.
3. **Actionable & Non-Destructive**: Never silently overwrites canvas work. Uses structured preview, approval, and inline annotations.
4. **Deterministic Canvas Execution**: Emits structured Figma operation primitives that construct native auto-layout components rather than uneditable flat vectors or bitmaps.

---

## 3. AZIA Personality & Interaction Philosophy

The user experience of AZIA is governed by strict personality heuristics configured in the core engine:

### 1. Balanced Critic (Strictness)
AZIA challenges weak reasoning with intellectual rigor, but remains supportive, constructive, and encouraging:
* *"I'm going to challenge that decision. You've identified a solution, but we haven't established the root problem yet."*
* *"From a cognitive load perspective, every extra screen or nested control adds drop-off risk. Let's explore if this step can be eliminated."*

### 2. Adaptive Mode (Conversation Style)
AZIA dynamically detects whether to answer directly, ask probing Socratic questions, teach a UX principle, or evaluate an edge case without forcing the designer to toggle rigid modes.

### 3. Subtle Humor & Warmth
AZIA communicates with character and wit without sacrificing executive professionalism:
* *"Hmm. Something smells fishy in this checkout flow. 🐟 Let's eliminate the friction before your users encounter it."*

### 4. Collaborator Canvas Control (Preview & Approve)
AZIA operates strictly on permission:
1. Analyzes requirement or canvas selection.
2. Formulates recommendations with confidence scores and evidence.
3. Provides a preview and explains *what* will change and *why*.
4. Awaits approval or refinement before applying changes to the Figma document.

---

## 4. End-to-End Autonomous UX Architecture Pipeline

AZIA's core pipeline (`azia/pipeline.py`) orchestrates a ten-stage cognitive design process:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       AZIA COGNITIVE DESIGN PIPELINE                        │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
           ┌───────────────────────────┴───────────────────────────┐
           ▼                                                       ▼
1. Requirement Engine                                   2. Socratic Sparring
   - JTBD & Persona Synthesis                              - Multi-provider LLM (Gemini/Grok)
   - Edge Cases & Constraints                              - Cognitive friction challenging
   - Primary & Secondary Success Metrics                   - Tone-adjusted critique
           │                                                       │
           └───────────────────────────┬───────────────────────────┘
                                       ▼
3. Information Architecture & Flow Engine
   - Topological Navigation DAG (Acyclic validation)
   - Screen-to-Screen entity mapping
   - Friction scoring & drop-off prevention
                                       │
                                       ▼
4. Design System & Token Synthesis
   - HSL-Tailored Color Harmony (Primary, Surface, Accent, State tokens)
   - WCAG 2.1 AA/AAA Contrast Verification (Formulaic luminance check)
   - Typography scales (Major Second / Major Third) & 4/8pt Spacing Grid
                                       │
                                       ▼
5. Component & Screen Architecture
   - Master component library (Buttons, Badges, Search, Cards, Inputs, Nav)
   - Auto-Layout responsive frames (Mobile 393x852px, Desktop 1280x900px)
   - State coverage (Default, Hover, Active, Empty, Error, Loading)
                                       │
                                       ▼
6. Synthetic Usability Simulation
   - Cognitive Load Index (CLI) scoring
   - Multi-persona walkthroughs (Student, Novice, Power User, Impaired)
   - Drop-off probability per transition
                                       │
                                       ▼
7. Automated UX Audit & Bounded Self-Repair Loop
   - Nielsen Heuristic evaluation (Slips, Mistakes, Visibility, Recognition)
   - Severity categorization (HIGH, MEDIUM, LOW)
   - Self-repair loop (auto-adjusts contrast or navigation if thresholds fail)
                                       │
                                       ▼
8. Deterministic Figma Operations Compiler
   - Compiles AST into sequential operations JSON
   - Emits canvas sections, master components, instances, and prototype wires
                                       │
                                       ▼
9. Multi-Target Code Generator
   - React 18 + Tailwind CSS components
   - SwiftUI native declarative views
   - W3C Design Tokens Studio JSON
```

---

## 5. Figma Plugin Architecture & Sandbox Engine

The AZIA Figma Plugin (`azia/plugin/`) connects the cloud AI intelligence directly into Figma's design environment via a secure, bi-directional IPC sandbox.

### Plugin Manifest & Security (`manifest.json`)
Conforms strictly to Figma's Plugin Manifest specification and Content Security Policy (CSP):
- **Allowed Network Domains**:
  - `https://uxui-agent.onrender.com` (AZIA Cloud Engine on Render)
  - `https://*.onrender.com`
  - `https://fonts.googleapis.com` & `https://fonts.gstatic.com` (Inter & Plus Jakarta Sans typography)
- **Dev Domains**: `http://localhost:8000` (Local fast iteration)
- **Editor Types**: `figma` and `figjam`

### Plugin UI Tabs (`ui.html`)
The 440×680px dark-mode interface (`#0F172A`) features 4 primary tabs:
1. **📋 Paste / Demo (Zero Network Fallback)**:
   - **🍔 CraveBite App**: 1-click rendering of 7 mobile delivery screens (80 operations). Pre-bundled offline payload that renders in 0ms with zero network requests.
   - **⚡ SprintFlow PM**: 1-click rendering of 4 desktop SaaS screens (47 operations) offline.
   - **JSON Paste Area**: Direct import for operations generated from the Web App or CLI.
   - **Undo / Rollback**: Instant clean removal of AZIA-tagged nodes using plugin metadata.
2. **🚀 Live AI API**:
   - Live endpoint configuration with **"Ping Test"** connection diagnostics (measures latency in ms and provides visual feedback for Render cold-starts).
   - Form factor selector (Mobile 393px vs Desktop 1280px) and visual directions.
   - Prompt input with quick-selection chips.
3. **🔍 UX Audit**:
   - Selection inspector: reads current canvas frame dimensions, name, and node type.
   - Displays severity-ranked Nielsen findings with **"+ Add Canvas Annotation"** affordance.
4. **💬 Socratic Sparring Partner**:
   - Interactive chat stream challenging assumptions, testing 3-step simplifications, and suggesting progressive disclosure.

### Execution Sandbox Layer (`dist/code.js`)
Translates JSON operations into native Figma nodes:
- **`create_section`**: Organizes work into 3 canvas milestones:
  1. *UX Architecture & Strategic Personas* (Sticky notes & JTBD)
  2. *Design Tokens & Master Components* (Button, Card, Search, Input primitives)
  3. *Interactive Connected Product* (Screens linked via prototype wires)
- **`create_screen`**: Auto-layout frames with section-relative coordinates and background fills.
- **`create_component`**: Generates master component symbols inside Section 2.
- **`create_instance`**: Instantiates rich, production-grade components into screen frames, populating titles, descriptions, price tags, ratings, status badges, and itemized bills.
- **`connect_prototype`**: Links interactive trigger events (`ON_CLICK` -> `NAVIGATE` with `DISSOLVE`) between screens.
- **Smart Screen Zoom**: Automatically focuses and zooms into the rendered product screens at 100% scale.

---

## 6. Verified Reference Domains & Design Benchmarks

AZIA's design engineering capabilities have been proven on two complex reference applications:

### Domain 1: CraveBite (Hyper-Local Campus Food Delivery)
* **Target Audience**: College students ordering late-night food to dorm landmarks.
* **Form Factor**: Mobile (393 × 852px, iPhone 16 Pro dimensions).
* **Palette**: Energetic Persimmon Orange (`#EA580C`), Slate Charcoal (`#0F172A`), Warm Cream (`#FAFAF9`), Mint Emerald (`#10B981`).
* **Architecture (7 Connected Screens)**:
  1. `scr_home`: Campus discovery feed, dorm landmark picker, student discounts, meal cards.
  2. `scr_search`: Real-time dietary filters (Halal, Vegan, Budget, Fast Delivery).
  3. `scr_restaurant_detail`: Customizable meal builder with spicy levels and topping add-ons.
  4. `scr_cart`: Cart review, dorm delivery spot selector, campus discount breakdown.
  5. `scr_checkout`: Frictionless payment options (Apple Pay, Campus Dining Card).
  6. `scr_order_confirmation`: Prep time summary, 4-digit pickup PIN, live tracking CTA.
  7. `scr_order_tracking`: Campus map simulation with bicycle courier ETA and direct chat.
* **Operations Count**: 80 deterministic Figma canvas operations.

### Domain 2: SprintFlow Workspace (B2B SaaS Developer PM)
* **Target Audience**: Engineering managers and tech leads tracking sprint velocity.
* **Form Factor**: Desktop Web (1280 × 900px).
* **Palette**: Deep Navy (`#0F172A`), Electric Indigo (`#3B82F6`), Clean Slate (`#F8FAFC`).
* **Architecture (4 Connected Screens)**:
  1. `scr_dashboard`: Project overview, burndown velocity metrics, active sprint squad stats.
  2. `scr_kanban_board`: Drag-ready Kanban board (Backlog, In Progress, Code Review, Done).
  3. `scr_create_task_modal`: Story point estimation, assignee dropdown, PR branch linker.
  4. `scr_task_detail`: Comprehensive drawer specification with commit logs and acceptance criteria.
* **Operations Count**: 47 deterministic Figma canvas operations.

---

## 7. Cloud Deployment & API Registry

AZIA is hosted on Render's container cloud (`https://uxui-agent.onrender.com`):

### API Endpoints
| Route | Method | Payload / Params | Response | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| `/health` | `GET` | None | `{"status": "ok", "engine": "ready", "ai": {...}}` | Health monitor and provider latency probe. |
| `/api/ai/status` | `GET` | None | Status of Gemini 3.8 Flash, xAI Grok, and active fallback. | Telemetry for AI engine status. |
| `/api/ai/configure` | `POST` | `{"gemini_api_key": "...", "grok_api_key": "..."}` | Confirmation and updated provider status. | Dynamic runtime key updates. |
| `/api/design` | `POST` | `{"requirement": "...", "platform": "...", "style": "..."}` | Complete product spec, audit report, and Figma JSON payload. | Primary autonomous design synthesis. |
| `/api/spar` | `POST` | `{"query": "...", "context": "..."}` | `{"critique": "...", "tone": "..."}` | Real-time Socratic sparring dialogue. |
| `/download-plugin` | `GET` | None | Binary `.zip` download (`azia-figma-plugin.zip`). | 1-click plugin distribution for any machine. |
| `/previews/{domain}/...` | `GET` | None | Static operations JSON payloads. | Verified architectural preview payloads. |

---

## 8. Automated Test Suite & Quality Verification

AZIA enforces strict software reliability via **28 automated tests** (`python -m pytest azia/tests -v`):
- `test_requirement_engine.py`: Tests persona and JTBD extraction for multiple domains.
- `test_ux_ia_flow.py`: Tests DAG topological sorting and navigation flow coherence.
- `test_design_system_and_screens.py`: Tests token generation, WCAG contrast verification, auto-layout parameters, and responsive resizing.
- `test_simulation_engine.py`: Tests synthetic user telemetry, cognitive load scoring, and friction heuristics.
- `test_qa_and_repair.py`: Tests Nielsen audit checks and automated self-repair loops.
- `test_renderer_operations.py`: Tests Figma operations compiler and virtual canvas collision prevention.
- `test_code_generator.py`: Tests clean React+Tailwind and SwiftUI component emission.
- `test_llm_client.py`: Tests Gemini and Grok API connectivity, fallback modes, and dynamic key configuration.
- `test_mcp_and_api.py`: Tests FastAPI routes, MCP protocol server tools, and `/download-plugin` zip streaming.
- `test_end_to_end_domains.py`: Full end-to-end synthesis of CraveBite and SprintFlow.

---

## 9. Future Roadmap: The Path to AZIA 2.0

With the core autonomous engine, web studio, and Figma plugin fully established, the future roadmap focuses on deeper design-to-production intelligence:

1. **Bi-Directional Canvas Reverse Engineering**:
   - Point AZIA at an existing messy Figma file.
   - Automatically extract existing color variables and components, reconstruct the user flow DAG, detect UX anti-patterns, and generate a structured PRD.
2. **Multi-Agent Review Board ("Run Design Committee")**:
   - Simultaneously evaluate designs from 4 specialized agent perspectives:
     - *Accessibility Specialist* (WCAG compliance)
     - *Growth Designer* (Conversion funnels & friction)
     - *Security & Privacy Lead* (Data exposure & permission slips)
     - *Systems Architect* (Component reuse & token drift)
3. **Live Product Telemetry Integration**:
   - Ingest live funnel drop-off analytics from PostHog, Amplitude, or Google Analytics to map real user abandonment directly onto corresponding Figma frames.
4. **Interactive Component Prototyping (Figma Variables & State Switching)**:
   - Deepen Figma export to create native Figma Variables (Boolean, Color, String, Number) and multi-state component sets (`ComponentSetNode`) with interactive variant transitions.
