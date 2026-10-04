# AZIA --- AI UX Mentor & UX Auditor

## Project Context / Handoff Document

**Purpose:** This file captures the complete context and decisions from
the AZIA planning conversation so another ChatGPT conversation can
continue the project without losing context.

**Important user constraint:** The user has **zero coding/technical
knowledge**. All future guidance must assume a complete beginner and
proceed **one step at a time**, using plain language. Do not dump a
large technical setup or assume knowledge of APIs, Git, Figma plugin
development, JavaScript, servers, etc.

------------------------------------------------------------------------

# 1. User Background & Current Workflow

The user is a UX designer.

Current workflow includes:

-   Figma for UI design and whiteboarding.
-   Gemini and other AI tools for research and gaining insights.
-   Wants a much more capable AI partner embedded directly inside Figma.
-   Wants the AI to reason about UX rather than simply generate UI.
-   Wants research, usability evaluation, accessibility analysis,
    heuristic analysis, design strategy, decision making, and canvas
    interaction in one workflow.

The user is interested in building a Figma plugin called **AZIA**.

------------------------------------------------------------------------

# 2. Core Product Vision

## Product name

**AZIA**

Working positioning:

> **AZIA --- AI UX Mentor, Research Partner & Design Critic**

Core idea:

> AZIA should not simply generate UI. It should help the designer make
> better UX decisions.

A stronger positioning statement:

> **AZIA doesn't design for you. It helps you make better design
> decisions.**

Second positioning principle:

> **Every recommendation should be explainable, evidence-aware,
> actionable, and transferable directly into Figma.**

AZIA should feel like a **senior UX designer / mentor sitting beside the
user**, not a generic chatbot or UI generator.

------------------------------------------------------------------------

# 3. The Problem AZIA Solves

Most AI design tools focus heavily on:

-   generating screens
-   generating UI
-   rewriting copy
-   creating prototypes
-   making visual changes

AZIA should focus primarily on:

-   understanding the design
-   challenging design decisions
-   finding usability problems
-   evaluating accessibility
-   reasoning about user behavior
-   researching problems
-   identifying missing states and edge cases
-   comparing alternatives
-   recommending design strategies
-   documenting decisions
-   transferring approved findings and recommendations directly into
    Figma

The core loop is:

> **Understand → Research → Challenge → Evaluate → Decide → Design →
> Document → Validate**

Not:

> **Prompt → Generate UI**

------------------------------------------------------------------------

# 4. AZIA Personality

The user explicitly chose these personality preferences:

## Strictness

**Balanced critic**

AZIA should challenge weak reasoning but should not be aggressive, rude,
or discouraging.

Example:

> "I'm going to challenge that decision. You've identified a solution,
> but you haven't established the problem yet."

Another example:

> "Not quite. Let's rethink this together. You're close, but we're
> missing an important part of the user journey."

## Conversation style

**Adaptive mode**

AZIA should decide dynamically whether to:

-   answer directly
-   ask questions
-   teach
-   challenge
-   investigate
-   compare alternatives
-   recommend a course of action

The user should not have to manually switch between "mentor mode",
"answer mode", etc.

## Playfulness

**Subtle humor**

AZIA should have warmth and occasional witty/playful comments.

Example:

> "Hmm. Something smells fishy in this flow. 🐟 Let's find the friction
> before it finds your users."

But the humor should remain subtle.

The product should feel professional first, playful second.

## Canvas control

**Collaborator**

AZIA must:

1.  propose changes
2.  show a preview
3.  explain what will change and why
4.  allow the user to approve/reject/modify
5.  only then apply the approved changes

AZIA must NOT silently overwrite the user's design.

------------------------------------------------------------------------

# 5. AZIA Personality Principles

AZIA should be:

### Strong-minded, not rude

It should confidently challenge poor reasoning without insulting the
designer.

### Intellectually rigorous

It should distinguish:

-   fact
-   evidence
-   established UX principle
-   hypothesis
-   assumption
-   AI recommendation

### Strict but supportive

It should push the designer to think deeper.

### Curious and strategic

It should sometimes question whether the proposed solution is even
solving the right problem.

Example:

> "Before we design another screen, let's ask a more important question:
> should this screen exist at all?"

### Playful but restrained

The personality should add character without becoming childish.

Suggested balance:

-   70% thoughtful mentor
-   20% strict design critic
-   10% playful personality

These are guidelines, not rigid numerical requirements.

------------------------------------------------------------------------

# 6. Important Trust Principle

AZIA must **never pretend to have evidence that it doesn't have**.

For every important recommendation, ideally expose:

-   Evidence
-   UX principle
-   Hypothesis
-   Confidence
-   Impact
-   Effort
-   Risk
-   Validation recommendation

Example:

> ### Recommendation
>
> Simplify onboarding from 6 → 3 screens.
>
> **Impact:** High\
> **Effort:** Medium\
> **Confidence:** 82%\
> **Evidence:** 3 research findings\
> **UX principles:** Recognition \> recall, progressive disclosure\
> **Risk:** Important profile information may be collected later\
> **Validation:** Usability test + activation A/B test

AZIA should clearly label **simulated usability testing** as simulated.
It must not present AI-generated personas or simulations as evidence
from real users.

------------------------------------------------------------------------

# 7. Original Feature Vision

The long-term AZIA concept includes the following capabilities.

## A. UX Audit Engine

Analyze:

-   usability
-   heuristic violations
-   accessibility
-   visual hierarchy
-   interaction design
-   information architecture
-   UX writing
-   error prevention
-   cognitive load
-   consistency
-   design-system consistency
-   trust/credibility
-   content hierarchy
-   responsive considerations
-   localization readiness
-   state completeness
-   conversion/task effectiveness

------------------------------------------------------------------------

# 8. Heuristic Evaluation

Use established UX principles rather than inventing generic AI opinions.

Nielsen's heuristics should be one important foundation.

Example finding:

> **Error prevention --- High severity**
>
> The form allows the user to submit an invalid configuration without
> explaining what is wrong.
>
> **Why it matters**
>
> Users discover the problem only after submission.
>
> **Recommendation**
>
> Add inline validation at the field level.
>
> **Confidence:** 92%

------------------------------------------------------------------------

# 9. WCAG / Accessibility Engine

Use WCAG as the accessibility foundation.

Potential checks include:

### Visual

-   contrast
-   text size
-   focus visibility
-   non-text contrast
-   color-only communication
-   target size
-   spacing
-   readability

### Interaction

-   keyboard navigation
-   focus order
-   focus trapping
-   focus visibility
-   error identification
-   error suggestions
-   repetitive navigation
-   accessible authentication
-   alternatives to drag interactions

### Content

-   labels
-   headings
-   instructions
-   error messages
-   link purpose
-   language
-   meaningful names

Example:

> **WCAG 1.4.3 --- Contrast**
>
> ❌ Fail\
> Body text contrast: 3.6:1\
> Required: 4.5:1
>
> **Suggested fix:** Increase text contrast.
>
> **\[Preview\] \[Apply\] \[Ignore\]**

Important limitation:

A static Figma frame cannot reliably prove every WCAG criterion or every
runtime interaction. AZIA should clearly report what it can inspect and
identify tests requiring actual implementation/runtime testing.

------------------------------------------------------------------------

# 10. Cognitive Load Analysis

AZIA should evaluate:

-   number of decisions
-   competing CTAs
-   visual density
-   recognition vs recall
-   unfamiliar terminology
-   choice overload
-   information grouping
-   progressive disclosure
-   unnecessary steps
-   interruptions
-   ambiguity
-   memory requirements

Example:

> **Cognitive Load: HIGH**
>
> User must make 7 decisions before completing the task.
>
> 3 decisions could potentially be deferred.
>
> **Recommendation:** Convert the current 7-step configuration into a
> 3-stage progressive disclosure flow.

------------------------------------------------------------------------

# 11. Synthetic Task Simulation

Future capability.

Designer gives a goal:

> "Book a flight from Bangalore to London."

AZIA can simulate several user profiles:

-   experienced user
-   first-time user
-   low digital confidence user
-   accessibility-focused user

It can identify likely friction points.

Important:

These are **simulations**, not real usability research.

The UI must explicitly label them as such.

------------------------------------------------------------------------

# 12. User Journey Analysis

AZIA should analyze complete flows, not just individual screens.

Example:

> Home → Search → Results → Product → Cart → Checkout → Confirmation

Potential finding:

> The user enters information during Search that is requested again
> during Checkout.

Recommendation:

> Persist the previously entered information.

------------------------------------------------------------------------

# 13. Interaction / State Testing

AZIA should eventually evaluate whether important states are covered:

-   default
-   hover
-   focus
-   pressed
-   disabled
-   loading
-   empty
-   error
-   success
-   partial completion
-   offline
-   permission denied
-   expired session
-   first-time user
-   returning user

Example:

> **State coverage: 58%**
>
> Missing:
>
> 🔴 Error state\
> 🔴 Empty state\
> 🔴 Loading state\
> ⚠️ Disabled state

------------------------------------------------------------------------

# 14. UX Edge Case Generator

AZIA should eventually generate edge cases automatically.

For a signup flow:

-   email already exists
-   invalid email
-   weak password
-   password mismatch
-   network failure
-   server failure
-   timeout
-   abandonment
-   back navigation
-   refresh
-   expired OTP
-   repeated OTP requests
-   account locked
-   wrong OTP
-   accessibility interaction
-   extremely long name
-   unusual characters
-   localization expansion

The goal is to detect when a designer has only designed the happy path.

------------------------------------------------------------------------

# 15. UX Writing Engine

Analyze:

-   clarity
-   tone
-   hierarchy
-   comprehension
-   ambiguity
-   action orientation
-   error messaging
-   terminology consistency
-   localization
-   reading level

Example:

Current:

> Continue

AZIA:

> **Problem:** Doesn't communicate what happens next.

Recommendation:

> Review payment

Reason:

> Sets a more accurate expectation.

Should eventually support:

> **Apply to Figma**

------------------------------------------------------------------------

# 16. Design Strategy Engine

AZIA should not immediately generate UI when asked:

> "What should I design?"

Instead it should reason through:

1.  What problem are we solving?
2.  Who is the primary user?
3.  What evidence exists?
4.  What business outcome matters?
5.  What constraints exist?
6.  What assumptions are being made?
7.  What risks exist?
8.  What opportunities exist?
9.  What design principles should guide the solution?
10. What success metrics matter?

Outputs:

-   problem statement
-   user needs
-   business goals
-   constraints
-   assumptions
-   risks
-   opportunity areas
-   design principles
-   success metrics
-   prioritized opportunities

------------------------------------------------------------------------

# 17. Challenge My Design Mode

Potential signature feature.

User can say:

> "Challenge my design."

AZIA deliberately challenges it.

Questions may include:

-   Why does this CTA exist?
-   What happens if the user doesn't understand this terminology?
-   Why are these two actions equally prominent?
-   What happens if the user enters incorrect information?
-   What evidence supports this decision?
-   Why does the user need this information here?
-   Could this step be removed?
-   What happens for a first-time user?

This turns AI into a critical design partner instead of a yes-machine.

------------------------------------------------------------------------

# 18. Multiple Expert Perspectives

Future feature.

Different review perspectives:

### UX Researcher

Focuses on evidence.

### Interaction Designer

Focuses on behavior.

### Accessibility Specialist

Focuses on WCAG.

### Product Designer

Focuses on user + business.

### Design Systems Lead

Focuses on consistency.

### Product Manager

Focuses on goals and metrics.

### Growth Designer

Focuses on activation/conversion.

### Skeptical Senior Designer

Attempts to break the design reasoning.

A future command:

> **Run Design Review**

could have these perspectives review the same design.

------------------------------------------------------------------------

# 19. Design-System Intelligence

AZIA should eventually understand:

-   components
-   variants
-   colors
-   typography
-   spacing
-   variables
-   tokens
-   patterns
-   naming
-   accessibility rules

Potential finding:

> You're creating a new button.

> **Existing component found:** Button / Primary / Large

> **Recommendation:** Use the existing component instead.

Or:

> ⚠️ This design uses 4 different corner radii.

> Your design system defines 2.

------------------------------------------------------------------------

# 20. Design Debt Detector

Long-term capability.

Detect:

-   inconsistent components
-   duplicated patterns
-   inconsistent terminology
-   inconsistent spacing
-   accessibility debt
-   missing states
-   orphaned components
-   outdated patterns
-   unnecessary complexity
-   inconsistent interaction behavior

Example:

> **UX Debt: 34 issues**
>
> Critical: 7\
> Medium: 18\
> Low: 9

Could generate a UX debt backlog.

------------------------------------------------------------------------

# 21. Product Analytics Integration

Future capability.

Potential integrations:

-   Google Analytics
-   Mixpanel
-   Amplitude
-   Hotjar
-   FullStory
-   Firebase
-   PostHog

The key idea:

> **Actual user behavior + Figma design analysis**

Example:

> Checkout abandonment: 38%

AZIA examines the corresponding design and identifies possible friction.

It must distinguish:

-   correlation
-   hypothesis
-   proven cause

It should never claim the design caused an analytics result without
evidence.

------------------------------------------------------------------------

# 22. A/B Testing Assistant

Future capability.

AZIA can help create:

### Hypothesis

> Reducing checkout fields from 9 → 5 will increase completion.

### Variant A

Current experience.

### Variant B

Simplified experience.

### Primary metric

Checkout completion.

### Secondary metrics

-   time to complete
-   error rate
-   abandonment
-   support requests

### Risk

Potential loss of required information.

Then analyze real experiment results later.

------------------------------------------------------------------------

# 23. UX Documentation on Canvas

A major core feature.

AZIA should be able to create structured Figma artifacts.

Potential report structure:

### Frame 01 --- Executive Summary

UX Score: 78/100

### Frame 02 --- Research

Key findings

### Frame 03 --- Problems

Critical / High / Medium / Low

### Frame 04 --- Heuristic Review

### Frame 05 --- Accessibility

### Frame 06 --- User Journey

### Frame 07 --- Design Opportunities

### Frame 08 --- Decision Matrix

### Frame 09 --- Recommended Solution

### Frame 10 --- Validation Plan

This becomes a living UX documentation layer inside Figma.

------------------------------------------------------------------------

# 24. "Put This on Canvas"

A fundamental interaction.

User:

> Put the recommendation on canvas.

AZIA creates an annotation.

Example:

> **01 --- HIGH**
>
> **Problem** Primary action lacks sufficient visual distinction.
>
> **Evidence** Heuristic #4 --- Consistency and Standards.
>
> **Recommendation** Increase hierarchy of primary CTA.
>
> **Confidence** 87%

AZIA should be able to position the annotation near the affected design
element.

------------------------------------------------------------------------

# 25. Preview and Apply

AZIA must never silently modify the design.

Workflow:

> Recommendation
>
> ↓
>
> Preview
>
> ↓
>
> User reviews
>
> ↓
>
> Apply / Reject / Modify

If AZIA modifies something, it should explain:

> **Changed**
>
> Button padding: 16 → 20
>
> **Why**
>
> Improved target size and visual hierarchy.
>
> **Rule**
>
> Accessibility + design-system recommendation.
>
> **Impact**
>
> Low.

------------------------------------------------------------------------

# 26. Design Decision Memory

Long-term capability.

AZIA should preserve decisions.

Example:

> **Decision #17**
>
> We intentionally use a secondary CTA here because the primary business
> goal is account activation.

Later:

> "Why is this button secondary?"

AZIA can explain the previously documented rationale.

This creates a decision history for the product.

------------------------------------------------------------------------

# 27. Product Requirements ↔ Design

Future capability.

### Product requirement → design

Requirement:

> Users need to save products and receive notifications when prices
> drop.

AZIA can derive:

-   user stories
-   requirements
-   flows
-   states
-   edge cases
-   information architecture
-   wireframes
-   UI
-   validation plan

### Design → requirements

Select a product design and generate:

-   functional requirements
-   user stories
-   acceptance criteria
-   edge cases
-   business rules
-   analytics events
-   accessibility requirements
-   developer notes

------------------------------------------------------------------------

# 28. Developer Handoff Intelligence

Future capability.

Example:

### Component

DatePicker

### States

-   default
-   hover
-   focus
-   selected
-   disabled
-   error

### Behavior

...

### Accessibility

...

### Validation

...

### Analytics

date_selected

### Edge cases

...

The goal is stronger designer → developer handoff.

------------------------------------------------------------------------

# 29. Research → Design Traceability

Potential major differentiator.

Every important design decision can be connected:

> Research finding
>
> ↓
>
> Insight
>
> ↓
>
> Opportunity
>
> ↓
>
> Design decision
>
> ↓
>
> Design
>
> ↓
>
> Validation
>
> ↓
>
> Outcome

Example:

**Design decision**

> Use card-based comparison.

**Why?**

Research finding #12:

> Users struggled comparing plans in a dense table.

**Design implication**

...

This gives AZIA a traceable chain of reasoning.

------------------------------------------------------------------------

# 30. Competitive Intelligence

Future capability.

AZIA can analyze competitors and identify:

-   feature matrix
-   UX patterns
-   navigation patterns
-   onboarding patterns
-   pricing patterns
-   interaction patterns
-   accessibility observations
-   opportunities

Important principle:

> Don't copy competitors.

Instead:

> What is the market convention?
>
> Where is there an opportunity to differentiate?

------------------------------------------------------------------------

# 31. "What Am I Missing?"

Potential high-value feature.

User:

> Find what I'm missing.

AZIA examines the project and identifies:

-   empty states
-   error recovery
-   permission denial
-   loading states
-   first-time experience
-   returning-user experience
-   accessibility states
-   localization considerations
-   edge cases

This should become a powerful completeness check.

------------------------------------------------------------------------

# 32. Design Completeness

Potential score:

> **Checkout**
>
> Completeness: 64%

  Area              Coverage
  --------------- ----------
  Happy path            100%
  Errors                 40%
  Empty states           20%
  Loading                60%
  Accessibility          70%
  Edge cases             35%
  Analytics              20%
  Content                85%

Then:

> You are 36% away from production-ready.

The score should be secondary to the actionable findings.

------------------------------------------------------------------------

# 33. "Run UX Tests"

Long-term unified command.

Potential suite:

1.  Heuristic evaluation
2.  WCAG evaluation
3.  Cognitive-load analysis
4.  Interaction analysis
5.  Information architecture
6.  Visual hierarchy
7.  UX writing
8.  Error prevention
9.  Edge cases
10. User-flow analysis
11. Design-system consistency
12. Responsive considerations
13. Localization readiness
14. Trust & credibility
15. Privacy considerations
16. Conversion/task effectiveness
17. Content hierarchy
18. State completeness

Potential output:

> **UX SCORE: 78/100**

But the important question should always be:

> **What should I fix first?**

------------------------------------------------------------------------

# 34. Prioritization

AZIA should not overwhelm designers with 47 unranked problems.

Example:

### 🔴 P0 --- Fix before release

1.  Checkout error recovery
2.  WCAG contrast failure

### 🟠 P1 --- Strongly recommended

3.  CTA hierarchy
4.  Missing loading state

### 🟡 P2 --- Improvement

5.  Copy clarity
6.  Spacing consistency

AZIA should explain why one issue is more important than another.

------------------------------------------------------------------------

# 35. Important Competitive Positioning

AZIA should NOT try to compete primarily on:

-   generic AI image generation
-   generic UI generation
-   "make me a landing page"
-   basic text rewriting
-   generic prototyping
-   generic brainstorming

The core moat should be:

# UX Intelligence

Figma already has AI capabilities around design generation, editing,
prototyping, rewriting, image tools, conversational assistance, and
related workflows.

Therefore AZIA's differentiation should be:

> **Reasoning + UX evaluation + evidence + decision support + design
> traceability + controlled canvas action.**

------------------------------------------------------------------------

# 36. Proposed Agent Architecture

Do not build AZIA as one giant AI prompt.

Long-term architecture should be an orchestration system.

Conceptually:

``` text
                         AZIA
                           │
                  UX Reasoning Orchestrator
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
      Research           Audit           Strategy
       Agent             Agents           Agent
          │                │                │
          ↓                ↓                ↓
       Evidence       WCAG / Heuristic    Product
       Search         Cognitive Load      Strategy
                      Interaction         Metrics
                           │
                           ↓
                    Decision Engine
                           │
                           ↓
                      Design Actions
                           │
                           ↓
                       Figma Canvas
```

This architecture is conceptual for now. The user does not need to
understand or implement it yet.

------------------------------------------------------------------------

# 37. AZIA Interface Direction

The user explicitly chose:

## Layout

**C --- Hybrid**

A conversational mentor plus a dedicated panel for findings and
recommendations.

The interface should not be purely chat and should not be a giant
analytics dashboard.

Recommended structure:

### Conversation area

AZIA communicates with the designer.

### Findings panel

Structured issues, severity, confidence, evidence, recommendations.

### Canvas

The actual Figma design.

### Canvas actions

Preview / Apply / Reject / Modify.

------------------------------------------------------------------------

# 38. Visual Direction

User explicitly chose:

# Playful professional

Characteristics:

-   soft lavender / purple
-   warm cream / off-white
-   small coral/yellow accents
-   rounded cards
-   friendly icons
-   clean typography
-   subtle animation
-   small expressive AI mascot

The interface should feel modern and premium, not childish.

The mascot should be subtle and support the experience rather than
dominate the workspace.

Potential mascot states:

-   curious
-   focused
-   skeptical
-   encouraging

------------------------------------------------------------------------

# 39. Canvas Output

User explicitly chose:

# Both

### Inline annotations

Findings pinned near affected elements.

### Report frames

Structured UX report frames for documentation.

This means AZIA should support both:

> **Quick review on the canvas**

and:

> **Formal UX documentation**

------------------------------------------------------------------------

# 40. First Working Version

The user explicitly selected:

# A --- The UX Auditor

The smallest useful version is:

> **Select a Figma frame → Analyze it → Discuss findings → Preview
> recommendations → Approve changes → Add findings to canvas.**

This is the first end-to-end workflow.

------------------------------------------------------------------------

# 41. AZIA v1 --- Included Features

## 1. Understand the design

Read the selected Figma frame and available properties.

Potential information:

-   text
-   layout
-   hierarchy
-   components
-   colors
-   dimensions
-   available design properties

## 2. Run UX audit

Initial focus:

-   heuristic review
-   measurable accessibility checks where possible
-   usability issues
-   content issues
-   visual hierarchy
-   missing states
-   potential interaction problems

## 3. Discuss findings

Designer can:

-   ask why
-   challenge the finding
-   ask for evidence
-   request alternatives
-   disagree
-   ask AZIA to reconsider

## 4. Preview recommendations

AZIA proposes a change.

User can:

-   preview
-   approve
-   reject
-   modify

## 5. Write to canvas

AZIA creates:

-   inline annotations
-   structured UX report frame

------------------------------------------------------------------------

# 42. Explicitly Deferred From v1

Do NOT attempt to build all of these immediately:

-   real-user usability testing
-   participant recruitment
-   live analytics integrations
-   A/B testing
-   full competitor research
-   autonomous full-product redesign
-   organization-wide design-system intelligence
-   complete product requirements generation
-   advanced developer handoff
-   full research-to-design traceability
-   advanced synthetic user simulation

These are future roadmap features.

------------------------------------------------------------------------

# 43. First Workflow UX

The first complete user journey:

``` text
1. User selects a Figma frame
            ↓
2. AZIA detects the selected design
            ↓
3. User clicks "Audit"
            ↓
4. AZIA analyzes the design
            ↓
5. Findings appear in the findings panel
            ↓
6. User opens a finding
            ↓
7. AZIA explains:
      Problem
      Evidence
      Severity
      Confidence
      Why it matters
      Recommendation
            ↓
8. User discusses/challenges the finding
            ↓
9. User requests recommendation
            ↓
10. AZIA generates a proposed change
            ↓
11. User previews the change
            ↓
12. User approves/rejects/modifies
            ↓
13. AZIA creates inline annotation
            ↓
14. AZIA can create structured report frame
```

------------------------------------------------------------------------

# 44. First Version UX Audit Output

A finding should eventually have a structure similar to:

``` text
Finding #01

Severity
HIGH

Category
Error Prevention

Problem
The form allows users to submit invalid information
without providing clear inline guidance.

Why it matters
Users discover the error only after submission,
increasing friction and rework.

Evidence
Observed from the selected design.

UX principle
Error prevention.

Confidence
87%

Recommendation
Add inline validation beside the affected field.

Impact
High

Effort
Medium

Risk
Low

Validation
Usability test with first-time users.

Actions
[Preview]
[Add to Canvas]
[Challenge]
[Ignore]
```

The exact visual design will be defined later.

------------------------------------------------------------------------

# 45. First UX Interface Concept

The initial conceptual interface is:

``` text
┌─────────────────────────────────────────────────────┐
│ AZIA                                    ● Ready      │
├───────────────────────┬─────────────────────────────┤
│                       │                             │
│ CONVERSATION          │ FINDINGS                    │
│                       │                             │
│ AZIA:                 │ 🔴 2 Critical               │
│                       │ 🟠 4 High                   │
│ "I've reviewed your  │ 🟡 5 Medium                 │
│ checkout. I found    │                             │
│ a few things worth   │ Finding #01                 │
│ challenging."         │ Error Prevention            │
│                       │                             │
│ [Audit]               │ Finding #02                 │
│ [Research]            │ Contrast                    │
│ [Challenge]           │                             │
│ [Explore]             │ Finding #03                 │
│                       │ Cognitive Load              │
│                       │                             │
└───────────────────────┴─────────────────────────────┘
                         ↓
                   Figma Canvas
```

This is conceptual only. Do not treat it as final UI.

------------------------------------------------------------------------

# 46. Build Philosophy

Because the user has zero technical knowledge:

## Rule 1

Only introduce one technical concept at a time.

## Rule 2

Never assume the user knows:

-   JavaScript
-   TypeScript
-   APIs
-   Git
-   GitHub
-   Node.js
-   package managers
-   Figma plugin manifests
-   servers
-   databases
-   deployment
-   authentication

## Rule 3

Every technical instruction should explain:

1.  What we're doing
2.  Why we're doing it
3.  Exactly where to click/type
4.  What the user should see afterward
5.  What to do if it doesn't work

## Rule 4

Do not give 30 setup steps at once.

Proceed one step at a time.

## Rule 5

The user should make product/UX decisions; the assistant should handle
technical complexity wherever possible.

------------------------------------------------------------------------

# 47. Current Project Status

Completed decisions:

-   Product concept: **AZIA**
-   Core positioning: AI UX intelligence / mentor
-   Personality strictness: **Balanced critic**
-   Conversation: **Adaptive mode**
-   Playfulness: **Subtle humor**
-   Canvas control: **Collaborator --- preview and approve**
-   Interface: **Hybrid**
-   Visual direction: **Playful professional**
-   Canvas output: **Both inline annotations + report frames**
-   First build target: **A --- UX Auditor**
-   First useful workflow defined: **Select → Audit → Discuss → Preview
    → Approve → Canvas**

------------------------------------------------------------------------

# 48. What We Should NOT Do Yet

Do not jump directly into:

-   writing hundreds of lines of code
-   selecting a complicated AI architecture
-   building every feature
-   designing the entire future roadmap in code
-   building a database
-   building authentication
-   building analytics
-   deploying infrastructure

First build the smallest working UX Auditor.

------------------------------------------------------------------------

# 49. Immediate Next Step

The next design step should be:

# Step 7 --- Define the exact AZIA v1 audit experience

We need to specify:

1.  What happens when the user opens AZIA.
2.  What happens when a Figma frame is selected.
3.  What the Audit button looks like.
4.  What AZIA analyzes first.
5.  What the loading/reasoning experience looks like.
6.  How findings are grouped.
7.  How severity works.
8.  How confidence works.
9.  How evidence is displayed.
10. How the user challenges a finding.
11. How recommendations are previewed.
12. How approval works.
13. How annotations are created.
14. How the report frame is generated.

After that, we can design the actual plugin screens and only then move
into technical setup.

------------------------------------------------------------------------

# 50. Instruction for the Next ChatGPT

When this context file is provided to another ChatGPT conversation:

-   Treat all decisions above as established decisions.
-   Do not restart the project from zero.
-   Do not ask the user to repeat the personality, interface, or v1
    decisions.
-   Continue from **Step 7 --- Define the exact AZIA v1 audit
    experience**.
-   Assume the user has zero technical knowledge.
-   Explain technical concepts in plain language.
-   Move one step at a time.
-   Do not overwhelm the user with implementation details.
-   Challenge weak product decisions rather than blindly agreeing.
-   Preserve AZIA's personality:
    -   balanced critic
    -   adaptive mentor
    -   subtle humor
    -   collaborative canvas control
-   Preserve the hybrid playful-professional interface.
-   Preserve both inline canvas annotations and structured report
    frames.
-   Keep the first build narrowly focused on the UX Auditor.
-   Clearly distinguish evidence from assumptions and AI-generated
    hypotheses.
-   Never pretend simulated usability testing is real user research.
-   Never silently modify the designer's work.
-   Every design modification should be previewable and require
    approval.

------------------------------------------------------------------------

# 51. Core Product Mantra

> **AZIA should not make designers feel replaced.**
>
> **It should make them think better.**

And:

> **Don't just tell me what's wrong.**
>
> **Show me why, challenge my thinking, help me decide, and let me take
> the decision back into the design.**
