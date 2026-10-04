# AZIA • Figma Integration Guide

Connect AZIA's autonomous design engine directly to your active Figma or FigJam canvas.

---

## ⚡ Step 1: Import the AZIA Plugin into Figma (30 Seconds)

1. Open the **Figma Desktop App** (or Figma in your browser with Figma Agent installed).
2. Open any design file or create a **New Design file**.
3. In the top-left corner, click the **Figma Menu (F icon)**:
   - Go to **Plugins** ➔ **Development** ➔ **Import plugin from manifest...**
   ![Figma Import](https://img.shields.io/badge/Figma-Import_From_Manifest-orange)
4. Browse to and select your project's manifest file:
   ```
   d:\PROJECTS-GITHUB\UXUI Agent\azia\plugin\manifest.json
   ```
5. Figma will immediately show:
   `"AZIA • AI UX Copilot & Autonomous Design MCP" imported.`

---

## 🚀 Step 2: Open and Run the Plugin

1. Right-click anywhere on the Figma canvas, or press `Shift + I` and select the **Plugins** tab.
2. Under **Development**, click **AZIA • AI UX Copilot & Autonomous Design MCP** and press **Run**.
3. The AZIA plugin panel will open docked next to your canvas.

---

## 🎨 Step 3: Render Designs to Your Canvas

### Method A: 1-Click Clipboard Sync from Web App (Instant)

1. Open the AZIA Web App (running locally at `http://localhost:8000` or on your Render URL).
2. Choose a product domain: **🍔 CraveBite (Mobile)** or **⚡ SprintFlow (Desktop SaaS)**.
3. In the right-hand panel under **🎨 Figma Live Sync**, click:
   ```
   📋 Copy Figma Operations JSON
   ```
4. Switch to Figma, open the AZIA Plugin, and select the **"📋 Paste / Demo"** tab.
5. Paste into the text box and click **"⚡ Render JSON to Figma Canvas"**!
6. All sections, screens, cards, and design tokens will immediately draw on your canvas with native Auto Layout!

---

### Method B: Live Generation Directly Inside Figma

1. In the AZIA Plugin, open the **"🚀 Live AI API"** tab.
2. Ensure your backend URL is set:
   - Local: `http://localhost:8000`
   - Render: `https://<your-service>.onrender.com`
3. Enter your prompt (e.g. *"Build an AI-native fitness tracking app"*).
4. Select Platform (*Mobile* or *Desktop Web*) and Visual Style.
5. Click **"✨ Generate & Render to Canvas"**.

---

### Method C: Run Nielsen UX Audits & Add Canvas Annotations

1. Select any screen, frame, or component on your Figma canvas.
2. In the plugin, go to the **"🔍 UX Audit"** tab.
3. Click **"🔎 Audit Selected Screen / Layer"**.
4. AZIA inspects the dimensions, hierarchy, and Auto Layout properties, running Nielsen Norman heuristics.
5. Click **"+ Add Canvas Annotation"** to drop a yellow sticky note pinned directly next to that frame on your canvas!

---

### Method D: Non-Destructive Rollback

AZIA tags every node it generates with `managed_by="autonomous-design-mcp"` and a unique `generation_id`.
- Click **"↩️ Rollback Last AZIA Generation"** at any time to cleanly remove only AZIA-generated frames without touching any of your personal design layers!

---

## 🔐 Security Reminder for API Keys

If you have a Google Gemini or xAI Grok API key:
- Copy `.env.example` to `.env`:
  ```bash
  cp azia/.env.example azia/.env
  ```
- Add your key to `azia/.env`.
- `.env` is already listed in `.gitignore`, protecting your private keys from being pushed to GitHub.
