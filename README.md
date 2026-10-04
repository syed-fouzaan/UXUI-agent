# AZIA • Autonomous AI Product Design & UX Copilot

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/syed-fouzaan/UXUI-agent)
[![Tests Passing](https://img.shields.io/badge/tests-28%2F28%20passing-brightgreen)](#)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

> **AZIA** is a production-grade Autonomous AI UX/UI Design Agent and Socratic Sparring Partner designed to operate at the skill level of a Senior Product Designer & Design Engineer.

---

## 🚀 1-Click Deploy to Render

Deploy the complete AZIA engine (interactive Web UI + REST API + AI Sparring + Synthetic Simulation Engine) to Render:

1. Click the **Deploy to Render** button above or go to [dashboard.render.com](https://dashboard.render.com).
2. Select **"Blueprint"** and link `https://github.com/syed-fouzaan/UXUI-agent.git`.
3. Render automatically detects [`render.yaml`](./render.yaml) and provisions the service.
4. *(Optional)* Add your free `GEMINI_API_KEY` or `GROK_API_KEY` in Environment Variables.

Detailed guide: [**Render Deployment Guide**](./azia/docs/RENDER_DEPLOYMENT.md).

---

## ✨ Key Capabilities

1. **Autonomous Product Design Pipeline**
   - Synthesizes user personas, JTBD, user flows, information architecture, design tokens, and components with 100% WCAG AAA accessibility compliance.
2. **Synthetic User Simulation & Visual Heatmaps**
   - Simulates 50+ user personas to predict drop-off rates and cognitive friction points before building.
3. **1-Click Production Code Handoff**
   - Clean React 18 + Tailwind CSS components, iOS SwiftUI views, and W3C DTCG standard tokens.
4. **Figma Design System Ingestion**
   - Ingests external design systems from Figma Tokens Studio, CSS Variables, and Tailwind themes.
5. **Senior Socratic Sparring Partner**
   - Real-time design critique powered by Google Gemini and xAI Grok APIs with offline heuristic fallback.
6. **Deterministic Figma Plugin Live Sync**
   - Generates deterministic JSON command payloads for instant 1:1 canvas sync.

---

## 📁 Repository Structure

```
.
├── azia/
│   ├── azia_core/         # Core AI design, simulation, and code generation engines
│   ├── web/               # Hosted interactive web application & prototypes
│   │   ├── index.html     # Main web app
│   │   └── previews/      # Interactive CraveBite & SprintFlow prototypes
│   ├── api_server.py      # FastAPI global backend service
│   ├── mcp_server.py      # Model Context Protocol (MCP) server
│   ├── requirements.txt   # Python dependencies
│   ├── render.yaml        # Render Blueprint configuration
│   └── tests/             # 28 comprehensive unit & integration tests
├── render.yaml            # Root Render Blueprint
├── requirements.txt       # Root Python requirements
├── Dockerfile             # Production container definition
└── README.md
```

---

## 💻 Local Quickstart

```bash
# 1. Clone repository
git clone https://github.com/syed-fouzaan/UXUI-agent.git
cd UXUI-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run test suite (28 tests)
python -m pytest azia/tests -v

# 4. Start local development server
python azia/api_server.py
```

Open `http://localhost:8000` to interact with AZIA in your browser!