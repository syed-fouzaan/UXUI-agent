# Hosting AZIA on Render • Step-by-Step Guide

AZIA is configured for **1-click automatic deployment** to [Render](https://render.com) as a Web Service.

When deployed, Render hosts:
1. **Interactive Product Design Web Canvas** at `/` (CraveBite Food Delivery & SprintFlow SaaS PM interactive prototypes)
2. **1-Click Production Code Handoff** (React + Tailwind, SwiftUI, W3C Tokens)
3. **Synthetic User Simulation & Visual Heatmaps**
4. **Figma Design System Ingestion** (Tokens Studio, CSS variables, Tailwind theme)
5. **Real-time Socratic Sparring Partner** connected to Google Gemini and xAI Grok APIs
6. **Full OpenAPI / Swagger API Explorer** at `/docs`
7. **Health Check Endpoint** at `/health`

---

## Method 1: 1-Click Render Blueprint (Recommended)

Render Blueprints use Infrastructure as Code via the included [`render.yaml`](../render.yaml).

1. Log in to [Render Dashboard](https://dashboard.render.com).
2. Click **"New +"** in the top navigation bar and select **"Blueprint"**.
3. Connect your GitHub repository:
   ```
   https://github.com/syed-fouzaan/UXUI-agent.git
   ```
4. Render will automatically read `render.yaml` and configure:
   - **Service Name:** `azia-uxui-agent`
   - **Runtime:** `Python 3.11`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn azia.api_server:app --host 0.0.0.0 --port $PORT`
   - **Health Check Path:** `/health`
5. Click **"Apply"**. Render will provision, build, and deploy AZIA in ~60-90 seconds.

---

## Method 2: Manual Web Service Setup on Render

If you prefer configuring via the web UI without Blueprints:

1. In [Render Dashboard](https://dashboard.render.com), click **"New +"** -> **"Web Service"**.
2. Select **"Build and deploy from a Git repository"** and choose `syed-fouzaan/UXUI-agent`.
3. Fill in the deployment parameters:

| Field | Value |
|---|---|
| **Name** | `azia-uxui-agent` |
| **Region** | Select closest to you (e.g. Frankfurt, Oregon, Ohio, Singapore) |
| **Branch** | `main` |
| **Root Directory** | *(Leave blank)* |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn azia.api_server:app --host 0.0.0.0 --port $PORT` |
| **Instance Type** | `Free` |

4. Scroll to **Advanced** -> **Health Check Path** and set:
   ```
   /health
   ```
5. *(Optional)* Add Environment Variables:
   - `GEMINI_API_KEY`: Your Google Gemini API Key
   - `GROK_API_KEY`: Your xAI Grok API Key
   - `PYTHON_VERSION`: `3.11.9`
6. Click **"Create Web Service"**.

---

## Method 3: Container / Docker Deployment

Render also supports Docker natively:
1. Select **"Docker"** runtime when creating the Web Service.
2. Render will automatically use the included [`Dockerfile`](../Dockerfile) and expose port `10000`.

---

## Verifying Your Live Deployment

Once Render finishes deploying (marked by a green badge and `Your service is live at https://<your-app>.onrender.com`):

1. **Interactive Visual UI:**
   Visit:
   ```
   https://<your-app>.onrender.com/
   ```
   - Switch between **🍔 CraveBite (Mobile App)** and **⚡ SprintFlow (Desktop SaaS)**.
   - Test **🔬 Synthetic Simulation & Heatmaps**, **💻 1-Click Code Handoff**, and **📥 Figma Ingestion**.
   - Spar with the **💬 Socratic Sparring Partner** in real-time.

2. **Interactive API Explorer & Swagger:**
   Visit:
   ```
   https://<your-app>.onrender.com/docs
   ```
   Try out any endpoint interactively:
   - `POST /api/design`
   - `POST /api/spar`
   - `POST /api/simulation`
   - `POST /api/code-handoff`
   - `POST /api/design-system/ingest`
   - `GET /health`

3. **Configuring AI Keys on the Live Instance:**
   - Either add `GEMINI_API_KEY` / `GROK_API_KEY` in the Render Environment Variables tab.
   - Or click the **"🔑 Set Gemini / Grok Key"** button right inside the live web header.
