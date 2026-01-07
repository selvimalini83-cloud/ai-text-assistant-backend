---
title: AI Text Assistant
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: app.py
---

# AI Text Assistant 🤖

This is a Flask-based AI Text Assistant that provides:
- Grammar correction
- Spam / Not Spam detection

## Backend
- Python
- Flask
- Scikit-learn

## Hosting
- Backend deployed on Hugging Face Spaces
- Public API access enabled

---

## Deploying to Hugging Face Spaces (single repo)
1. Create a new **Space** on Hugging Face (select "Gradio / Streamlit / Other" as appropriate).
2. Push this repository to the Space's Git URL (or connect to a GitHub repo).
3. Make sure `requirements.txt` contains all dependencies (done).
4. Optionally set `HF_API_TOKEN` in the Space's secrets to use the Hugging Face Inference API for grammar correction (recommended to avoid large model downloads in the Space):
   - Go to the Space settings -> Secrets -> Add `HF_API_TOKEN` with a token from your HF account.
5. The Space will run the `Procfile` or `start.sh` by default; the app serves both the frontend (static files under `frontend/`) and API endpoints.

### Notes
- If you do not set `HF_API_TOKEN`, the app will try to load the grammar model locally in a background thread; this may take time or fail due to disk/ram limits.
- Endpoints:
  - `GET /health` — check readiness
  - `POST /predict-spam` — JSON {"text": "..."}
  - `POST /grammar` — JSON {"text": "..."}

---

