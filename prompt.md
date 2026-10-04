MASTER IMPLEMENTATION PROMPT
=============================

You are the principal software architect, AI engineer, Figma plugin engineer,
MCP engineer, UX architect, and QA engineer responsible for building the
Autonomous Figma Product Design MCP.

Your job is to BUILD THE COMPLETE WORKING PRODUCT described below.

Do not merely explain the architecture.
Do not generate a tutorial.
Do not create a mockup.
Do not create a proof of concept that stops at scaffolding.
Do not leave core functionality as TODOs.
Do not repeatedly ask me for implementation decisions.

Make reasonable engineering decisions yourself and continue until the
acceptance criteria are satisfied.

============================================================
1. PRODUCT
============================================================

Build an autonomous AI design engineer that takes a natural-language product
requirement and automatically creates a complete editable Figma product.

The core user experience is:

    User
      |
      | "Build a food delivery app for college students..."
      |
      v
    DESIGN MCP
      |
      +--> Understand requirement
      |
      +--> Identify users
      |
      +--> Define UX
      |
      +--> Define information architecture
      |
      +--> Define user journeys
      |
      +--> Determine screens
      |
      +--> Determine layouts
      |
      +--> Determine components
      |
      +--> Create design system
      |
      +--> Generate content
      |
      +--> Build Figma design
      |
      +--> Connect prototype
      |
      +--> Generate states
      |
      +--> Perform visual QA
      |
      +--> Perform UX QA
      |
      +--> Automatically repair issues
      |
      v
    COMPLETE EDITABLE FIGMA DESIGN

The user should NOT have to say:

"Create a frame."

"Create a card."

"Create a button."

"Create screen 2."

"Connect screen 3 to screen 4."

"Add empty state."

"Fix spacing."

The system must determine all of these automatically.

============================================================
2. THE CORE PROMISE
============================================================

The entire product must optimize for this:

ONE REQUIREMENT
       +
ONE COMMAND
       =
COMPLETE PRODUCT DESIGN

The primary MCP capability must be:

    design_product

Example:

    design_product(
        requirement="""
        Build a modern food delivery app for college students.
        Students should discover nearby restaurants, search food,
        order food, pay, and track delivery.
        The experience should be fast, affordable and simple.
        """
    )

After this command, the system should autonomously execute the entire
design pipeline.

============================================================
3. DO NOT BUILD A CHATBOT
============================================================

This is NOT primarily a conversational UX assistant.

It is an AUTONOMOUS DESIGN ENGINE.

The AI should reason internally and produce a structured design specification.

The structured specification is then converted into deterministic Figma
operations.

Architecture:

    Requirement
         |
         v
    AI Planning
         |
         v
    Design Specification
         |
         v
    Schema Validation
         |
         v
    Operation Planner
         |
         v
    Deterministic Renderer
         |
         v
    Figma Plugin API
         |
         v
    Figma

NEVER allow the LLM to generate arbitrary Figma API code and execute it.

============================================================
4. HIGH-LEVEL ARCHITECTURE
============================================================

Build these major subsystems:

    1. MCP Server
    2. Requirement Intelligence
    3. UX Architecture Engine
    4. Information Architecture Engine
    5. User Flow Engine
    6. Screen Planning Engine
    7. Component Planning Engine
    8. Design System Engine
    9. Content Generation Engine
   10. Design Specification Engine
   11. Operation Validation Engine
   12. Figma Rendering Engine
   13. Prototype Engine
   14. Existing Figma Context Engine
   15. Visual QA Engine
   16. UX/Requirement QA Engine
   17. Self-Repair Engine
   18. Persistence/Generation Management
   19. Logging/Observability

Keep these modules separated.

============================================================
5. RECOMMENDED STACK
============================================================

Backend:

- Python
- FastAPI
- Pydantic
- MCP-compatible server implementation

AI:

- Provider abstraction
- Ollama/local model support
- Optional cloud model providers
- Structured JSON generation

Figma:

- TypeScript
- Figma Plugin API
- React for plugin UI
- Vite

Database:

- PostgreSQL
- pgvector where semantic retrieval is needed

Testing:

- Pytest
- Vitest

Infrastructure:

- Docker Compose
- .env configuration

Everything must be runnable locally.

============================================================
6. MCP TOOLS
============================================================

The MCP must expose:

PRIMARY:

    design_product

SECONDARY:

    analyze_figma
    inspect_selection
    modify_product
    regenerate_screen
    regenerate_flow
    regenerate_component
    run_design_qa
    apply_design_fix
    get_generation_status
    rollback_generation

The primary tool must be capable of completing the entire workflow without
requiring the secondary tools.

============================================================
7. design_product INPUT
============================================================

Support a structure similar to:

{
    "requirement": "string",

    "platform": "auto | web | mobile | tablet | desktop",

    "fidelity": "low | medium | high",

    "style": "auto | minimal | modern | enterprise |
              playful | premium",

    "existing_figma_context": true,

    "autonomous": true
}

The system must work even when optional values are omitted.

If platform is "auto", infer the platform from the requirement.

If style is "auto", derive an appropriate visual direction.

============================================================
8. REQUIREMENT INTELLIGENCE
============================================================

The first agent must understand the requirement.

Extract:

- product name
- product category
- product purpose
- target users
- user goals
- business objective
- core tasks
- entities
- actions
- constraints
- platform
- important terminology
- success criteria

Every extracted item must be classified as:

    CONFIRMED
    INFERRED
    ASSUMPTION
    UNKNOWN

Never silently hallucinate requirements.

When information is genuinely missing, make a reasonable UX assumption and
mark it as ASSUMPTION.

Do not stop the entire generation process simply because the requirement is
not perfectly specified.

============================================================
9. UX ARCHITECTURE
============================================================

Determine:

- primary persona
- secondary personas where relevant
- Jobs-to-be-Done
- primary user goals
- user pain points
- primary journey
- secondary journeys
- entry points
- key actions
- success states
- failure states

Do NOT generate unnecessary personas or UX artifacts simply to make the
output look sophisticated.

Everything must serve the actual product.

============================================================
10. INFORMATION ARCHITECTURE
============================================================

Determine:

- global navigation
- page hierarchy
- content hierarchy
- major sections
- entities
- relationships
- navigation patterns
- screen groups

Do not hard-code screen lists.

The requirement determines the product.

============================================================
11. USER FLOW ENGINE
============================================================

Build complete user journeys.

Example:

    Landing
      |
    Sign Up
      |
    Verification
      |
    Onboarding
      |
    Home
      |
    Search
      |
    Results
      |
    Details
      |
    Cart
      |
    Checkout
      |
    Confirmation
      |
    Tracking

But DO NOT hard-code this example.

The engine must dynamically generate the appropriate flow for every
requirement.

Detect:

- dead ends
- missing transitions
- missing confirmation states
- missing error states
- unnecessary steps
- impossible transitions
- missing back navigation
- missing primary actions

============================================================
12. SCREEN PLANNING
============================================================

For every required screen generate:

    screen_id
    screen_name
    purpose
    user_goal
    entry_conditions
    exit_actions
    primary_cta
    secondary_actions
    content_hierarchy
    layout
    components
    states
    navigation
    prototype_destinations

The engine determines how many screens are necessary.

Do not artificially limit the number of screens.

Do not create unnecessary screens.

============================================================
13. COMPONENT ENGINE
============================================================

Implement reusable semantic components.

At minimum support:

- Button
- IconButton
- Input
- Search
- Select
- Checkbox
- Radio
- Toggle
- Card
- List
- Grid
- Navbar
- Sidebar
- Tabs
- Breadcrumbs
- Badge
- Avatar
- Modal
- Dialog
- Bottom Sheet
- Form
- Table
- Banner
- Alert
- Tooltip
- Pagination
- Progress
- Chart
- Loading
- Empty State
- Error State
- Success State

The engine must reuse components.

If ten screens need the same button style, create one component and use
instances/variants rather than manually drawing ten unrelated buttons.

============================================================
14. DESIGN SYSTEM ENGINE
============================================================

Automatically generate:

COLORS

- primary
- secondary
- background
- surface
- text
- muted
- border
- success
- warning
- error

TYPOGRAPHY

- display
- heading
- body
- caption
- label

SPACING

- xs
- sm
- md
- lg
- xl
- 2xl

OTHER:

- radius
- shadows
- borders
- grid
- container widths
- component dimensions
- icon sizing

Every screen must use the same design system.

Do not randomly invent styling for every screen.

============================================================
15. LAYOUT ENGINE
============================================================

The layout engine is a critical part of the product.

It must reason about:

- hierarchy
- importance
- visual weight
- whitespace
- alignment
- grouping
- CTA prominence
- density
- responsive behavior
- Auto Layout

Use:

- Auto Layout
- constraints
- component instances
- reusable structures

The layout must look intentionally designed.

Do not simply stack rectangles vertically.

============================================================
16. CONTENT ENGINE
============================================================

Generate realistic content.

BAD:

    Card title
    Description here
    Lorem ipsum

GOOD:

    "Chicken Biryani"
    "Aromatic basmati rice with tender chicken..."
    "₹149"
    "25–30 min"

Content must be relevant to the actual domain.

============================================================
17. UI STATE ENGINE
============================================================

Where relevant, automatically create:

- default
- hover
- focused
- selected
- disabled
- loading
- empty
- error
- success
- validation error
- offline
- permission denied

Do not blindly generate every state for every component.

Determine relevance from context.

============================================================
18. DESIGN SPECIFICATION
============================================================

Before touching Figma, produce an internal structured design specification.

Conceptually:

{
    "product": {},
    "personas": [],
    "jtbd": [],
    "flows": [],
    "navigation": {},
    "screens": [],
    "components": [],
    "design_system": {},
    "content": {},
    "states": [],
    "prototype": {},
    "assumptions": [],
    "operations": []
}

Validate it using Pydantic or equivalent schema validation.

If invalid:

    repair specification
    validate again

Do not send invalid specifications to the renderer.

============================================================
19. SEMANTIC FIGMA OPERATIONS
============================================================

Create deterministic operations such as:

    create_page
    create_section
    create_screen
    create_frame
    create_auto_layout
    create_text
    create_component
    create_component_variant
    create_instance
    create_button
    create_input
    create_card
    create_list
    create_grid
    create_navigation
    create_modal
    create_form
    create_table
    create_badge
    create_state
    connect_screen
    apply_design_tokens
    update_screen
    update_component
    replace_flow
    delete_generated_content

Each operation must have a strict schema.

============================================================
20. DETERMINISTIC FIGMA RENDERER
============================================================

The renderer receives validated operations.

Example:

    {
        "operation": "create_card",
        "id": "restaurant_card",
        "parent": "restaurant_grid",
        "layout": {
            "direction": "vertical",
            "padding": 16,
            "gap": 12
        }
    }

The renderer converts this into actual Figma nodes.

The renderer must:

- create real frames
- create real text
- create real components
- create instances
- use Auto Layout
- preserve editability
- apply design tokens
- maintain naming
- maintain hierarchy

Never flatten the UI into screenshots.

============================================================
21. FIGMA PLUGIN
============================================================

Build the Figma plugin as the execution layer.

It must support:

- MCP/backend communication
- selection inspection
- page inspection
- node creation
- node modification
- component creation
- Auto Layout
- styles
- variables/tokens where supported
- prototype connections
- generated-node metadata

The plugin must not contain the product intelligence.

The intelligence belongs to the MCP/backend.

============================================================
22. EXISTING FIGMA FILES
============================================================

If the user opens an existing Figma file:

Inspect relevant context before generating.

Look at:

- current page
- current selection
- existing components
- typography
- colors
- spacing
- styles
- variables
- naming conventions
- existing flows

Reuse existing design patterns where appropriate.

Do NOT destroy unrelated content.

============================================================
23. GENERATED CONTENT OWNERSHIP
============================================================

Every generated node should contain enough metadata to identify:

    product_id
    generation_id
    screen_id
    component_id
    managed_by

Example:

    managed_by = "autonomous-design-mcp"

This enables future operations such as:

    "Regenerate checkout."

    "Replace the home screen."

    "Remove the generated onboarding."

without affecting unrelated Figma work.

============================================================
24. PROTOTYPE ENGINE
============================================================

Automatically connect meaningful interactions.

Examples:

    Login button -> Home
    Search -> Search results
    Product card -> Product detail
    Add to cart -> Cart
    Checkout -> Payment
    Payment success -> Confirmation
    Track order -> Tracking

Do not create fake/random connections.

Every connection should correspond to a real user action.

============================================================
25. VISUAL QA ENGINE
============================================================

After generation, inspect the resulting design.

Check:

- alignment
- spacing
- hierarchy
- typography
- contrast
- overflow
- consistency
- component reuse
- navigation
- visual density
- missing elements
- broken layouts

If screenshots/rendered previews are available, use them.

The QA engine should return:

{
    "severity": "high | medium | low",
    "screen": "screen_id",
    "issue": "...",
    "evidence": "...",
    "recommended_fix": "..."
}

============================================================
26. UX / REQUIREMENT QA
============================================================

Do not only check visual quality.

Check whether the design actually satisfies the original requirement.

For example:

Requirement:

"Users can search restaurants and track delivery."

QA must verify that:

- search exists;
- restaurant results exist;
- restaurant details exist;
- ordering path exists;
- order confirmation exists;
- tracking exists.

Create requirement coverage analysis.

============================================================
27. SELF-REPAIR
============================================================

The system must NOT stop immediately after generation.

Run:

    GENERATE
       |
       v
    INSPECT
       |
       v
    FIND ISSUES
       |
       v
    PRIORITIZE
       |
       v
    GENERATE FIX OPERATIONS
       |
       v
    APPLY
       |
       v
    INSPECT AGAIN
       |
       v
    PASS

Use a bounded repair loop.

Example:

MAX_REPAIR_ITERATIONS = 3

If issues remain after the limit:

return a structured report instead of looping forever.

============================================================
28. MCP RESPONSE
============================================================

After design generation, return a structured summary:

    product
    generation_id
    screens_created
    components_created
    flows_created
    assumptions
    qa_score
    issues_fixed
    remaining_issues
    figma_context

The MCP response should be concise.

The actual design should exist in Figma.

============================================================
29. PROJECT STRUCTURE
============================================================

Use a structure similar to:

root/

    mcp/
        server.py
        tools/
        schemas/
        prompts/

    engine/
        requirement/
        ux/
        ia/
        flows/
        screens/
        components/
        design_system/
        content/
        prototype/
        qa/

    renderer/
        operations/
        validation/
        planning/

    plugin/
        src/
            code.ts
            ui.tsx
            api.ts
            types.ts
            figma/
        manifest.json
        package.json
        vite.config.ts

    tests/

    docs/

    data/

    docker-compose.yml
    .env.example
    README.md
    ARCHITECTURE.md
    MCP.md
    FIGMA.md
    TESTING.md

Keep responsibilities separated.

============================================================
30. TESTING
============================================================

Create unit tests for:

- requirement parsing
- classification
- UX planning
- flow generation
- screen planning
- component planning
- design tokens
- specification validation
- operation validation
- renderer
- metadata
- QA

Create integration tests for:

    requirement
        ->
    design specification
        ->
    validated operations
        ->
    renderer

Test at least TWO completely different product requirements.

Example:

1. Food delivery
2. Project management SaaS

The architecture must work generically.

Do not hard-code the food delivery example.

============================================================
31. ERROR HANDLING
============================================================

Handle:

- invalid requirement
- incomplete requirement
- LLM failure
- malformed model output
- invalid schema
- unsupported Figma operation
- Figma plugin unavailable
- renderer error
- QA failure
- timeout
- network failure

Never silently fail.

Return actionable errors.

============================================================
32. SECURITY
============================================================

Never execute arbitrary LLM-generated code.

Never evaluate model output as Python or JavaScript.

Use structured operations only.

Validate:

- operation type
- target
- parameters
- ownership
- destructive behavior

Destructive operations should require explicit confirmation unless the
operation only affects generated content owned by the current generation.

============================================================
33. OBSERVABILITY
============================================================

Implement structured logging.

Track:

    generation_id
    request_id
    requirement
    planning_duration
    rendering_duration
    number_of_screens
    number_of_components
    QA_issues
    repair_iterations
    final_status

Do not log secrets.

============================================================
34. DEVELOPMENT WORKFLOW
============================================================

Build incrementally.

PHASE 1

Create repository structure.

PHASE 2

Implement schemas.

PHASE 3

Implement requirement engine.

PHASE 4

Implement UX/IA/flow planning.

PHASE 5

Implement screen/component/design-system planning.

PHASE 6

Implement design specification validation.

PHASE 7

Implement semantic operation engine.

PHASE 8

Implement Figma plugin.

PHASE 9

Implement deterministic renderer.

PHASE 10

Implement prototype generation.

PHASE 11

Implement QA.

PHASE 12

Implement self-repair.

PHASE 13

Implement MCP integration.

PHASE 14

Run end-to-end tests.

PHASE 15

Polish and document.

Do not stop after any phase.

Continue until the complete acceptance criteria are met.

============================================================
35. FIRST END-TO-END TEST
============================================================

Use this requirement:

"Build a modern food delivery app for college students.
Students should be able to discover nearby restaurants,
search food, order food, pay, and track delivery.
The experience should be fast, affordable and simple."

Run:

    design_product(requirement)

Verify that the system automatically determines an appropriate design.

It should produce a complete editable Figma product with:

- navigation
- home
- discovery
- search
- results
- detail
- ordering
- cart
- checkout/payment
- confirmation
- tracking
- appropriate states
- reusable components
- design system
- connected prototype
- realistic content

The exact screens must be determined by the engine.

============================================================
36. SECOND END-TO-END TEST
============================================================

Test:

"Build a project management SaaS for small engineering teams.
Teams should create projects, manage tasks, assign work, track progress,
and see project status."

The system should automatically produce a completely different but
coherent product.

If the architecture only works for food delivery, it is considered a failure.

============================================================
37. DEFINITION OF DONE
============================================================

The implementation is NOT complete until:

[ ] MCP starts successfully
[ ] design_product is callable
[ ] requirement understanding works
[ ] UX planning works
[ ] IA planning works
[ ] flow planning works
[ ] screen planning works
[ ] component planning works
[ ] design-system generation works
[ ] content generation works
[ ] design specification validates
[ ] semantic operations validate
[ ] Figma plugin works
[ ] Figma nodes are created
[ ] nodes remain editable
[ ] Auto Layout is used
[ ] components are reusable
[ ] prototype connections work
[ ] states are generated
[ ] visual QA works
[ ] requirement QA works
[ ] self-repair works
[ ] generated nodes are identifiable
[ ] unrelated Figma content is preserved
[ ] two different product domains work
[ ] tests pass
[ ] documentation exists
[ ] local setup works
[ ] end-to-end generation works

============================================================
38. FINAL ENGINEERING PRINCIPLE
============================================================

Never optimize for:

"AI produced something that looks like a design."

Optimize for:

"AI understood the product and engineered a coherent, editable,
connected, reusable, validated Figma product."

The final system should feel like:

    AI Product Designer
          +
    UX Architect
          +
    UI Designer
          +
    Design System Engineer
          +
    Figma Engineer
          +
    QA Engineer

operating through ONE autonomous command.

The user says:

    "Build this product."

The system does everything else.

============================================================
39. FINAL INSTRUCTION
============================================================

START BUILDING NOW.

First inspect the repository and existing files.

If an existing implementation exists, preserve useful work and extend it
instead of unnecessarily rewriting it.

Create the architecture.

Implement the core schemas.

Implement the engines.

Implement the MCP.

Implement the Figma plugin.

Implement the renderer.

Implement QA.

Implement self-repair.

Run tests.

Fix failures.

Run the end-to-end examples.

Fix failures again.

Do not stop at documentation.

Do not stop at scaffolding.

Do not ask me to manually implement missing core pieces.

Continue until the complete system described above is operational.