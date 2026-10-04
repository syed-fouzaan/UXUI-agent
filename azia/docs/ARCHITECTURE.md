# AZIA System Architecture & Technical Specification

## 1. Overview
**AZIA (Autonomous Zero-Friction Interface Architecture)** is an autonomous AI product design engineering system and Model Context Protocol (MCP) server. Given a single natural-language requirement, AZIA orchestrates the full end-to-end UX/UI lifecycle:
- Requirement Intelligence & Epistemic Taxonomy
- Empathy Modeling, Personas & Jobs-to-be-Done (JTBD)
- Information Architecture, Screen Grouping & Navigation Models
- Graph-Based User Flows & Topological Health Validation
- 8-Point Spatial Grid Design Systems & WCAG 2.1 AA/AAA Tokens
- Semantic Component Registries & Variant Matrices
- Auto Layout Screen Inventories & Realistic Domain Copy
- Interactive Prototype Graphs & Animation Connections
- Non-Disruptive Launch Strategy & Safe Fallback Workflows
- Nielsen 10 Usability Heuristics & Accessibility Audits
- Dual-Track Visual/UX QA & Bounded Automated Self-Repair
- Deterministic Semantic Figma Operation Planning & Virtual Canvas DOM

```
Natural Language Requirement
           │
           ▼
┌──────────────────────────────────────────────┐
│          AZIA PRE-FLIGHT CHECK ENGINE        │
│  - Ambiguity detector & Context sufficiency  │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│        REQUIREMENT INTELLIGENCE & TAXONOMY   │
│  - CONFIRMED, INFERRED, ASSUMPTION, UNKNOWN  │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│          UX & INFORMATION ARCHITECTURE       │
│  - Behavioral Personas & JTBD Formulas       │
│  - Global Navigation & Screen Groupings      │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│         GRAPH USER FLOW ENGINE               │
│  - Happy paths, Edge cases, Decision nodes   │
│  - Dead-end & Unreachable node validation    │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│      DESIGN SYSTEM & COMPONENT REGISTRY      │
│  - 8pt Spatial Scale, WCAG AA/AAA Colors     │
│  - 30+ Semantic Auto Layout Components       │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│        SCREEN PLANNING & CONTENT ENGINE      │
│  - Auto Layout Sections & Component Binds    │
│  - Zero Dummy Text (Hyper-Realistic Content) │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│       PROTOTYPE & NON-DISRUPTIVE LAUNCH      │
│  - Clickable Interaction Graph (Slide/Smart) │
│  - Progressive Disclosure & Safe Fallbacks   │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│          NIELSEN AUDIT & QA ENGINE           │
│  - 10 Heuristics, WCAG Contrast, 8pt Grid    │
│  - Requirement Coverage Analysis (100%)      │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│      BOUNDED SELF-REPAIR OPTIMIZATION        │
│  - Inspect -> Fix -> Verify (Max 3 Loops)    │
└──────────────────────┬───────────────────────┘
                       │
                       ▼
┌──────────────────────────────────────────────┐
│      DETERMINISTIC FIGMA RENDERER LAYER      │
│  - Semantic Operation Planner                │
│  - Virtual Canvas DOM (Scene Graph)          │
│  - Figma Plugin API (`code.ts` sandbox)      │
│  - Non-Destructive Tagging (`managed_by`)    │
└──────────────────────────────────────────────┘
```

---

## 2. Epistemic Taxonomy & Zero Hallucination Principle
Current AI tools jump directly from prompt to screens, making hidden assumptions that disrupt established user mental models. AZIA enforces strict epistemic classification:

| Epistemic Tier | Description | Requirement Handling |
| :--- | :--- | :--- |
| **CONFIRMED** | Directly stated in user input or uploaded documentation | Kept intact as core design constraints |
| **INFERRED** | Logically deduced from industry patterns and platform conventions | Exposed with reasoning rationale |
| **ASSUMPTION** | Design hypotheses requiring field validation | Documented in `EpistemicRegister` with recommended validation method |
| **UNKNOWN** | Unspecified critical design variables | Flagged in Pre-Flight Check with targeted questions |

---

## 3. Semantic Figma Operations Protocol
AZIA never executes unvalidated or arbitrary LLM-generated code inside Figma. Instead, all changes are emitted as strictly typed, validated semantic operations:

- `create_page`
- `create_section`
- `create_screen`
- `create_frame`
- `create_auto_layout`
- `create_text`
- `create_component`
- `create_instance`
- `create_button`
- `create_input`
- `create_card`
- `create_sticky_note`
- `create_connector`
- `connect_prototype`
- `delete_generated_content`

### Non-Destructive Ownership
Every generated node is permanently stamped with metadata:
- `managed_by = "autonomous-design-mcp"`
- `generation_id = "<UUID>"`
- `product_id = "<PRODUCT_ID>"`

This allows AZIA to modify, regenerate, or rollback entire features without touching or corrupting the designer's manual work.
