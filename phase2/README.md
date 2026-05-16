# PromoCatch - Phase 2

PromoCatch is a campaign and deal tracking system built as a layered REST API.  
Phase 2 is the final version of the project and includes the complete web interface, backend API, SAD documents, screenshots, and presentation files.

## What This Phase Includes

- Full frontend for listing, searching, filtering, creating, updating, and deleting campaigns
- Full backend implementation with FastAPI
- SQLite persistence
- SAD Phase 1 and SAD Phase 2 documents
- Local presentation and screenshots
- Docker deployment files

## Architecture

The project follows a layered architecture:

- Presentation Layer: `static/index.html`
- Control Layer: `main.py`, `routers.py`
- Domain Layer: `schemas.py`, `services.py`
- Resource Layer: `database.py`, `models.py`, `repository.py`

## Technology Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- HTML, CSS, Bootstrap
- Vanilla JavaScript

## Quick Start for Windows

This is the easiest way to run the project on Windows.

1. Open the `phase2` folder.
2. Double-click `run_local.bat`.
3. Wait until the terminal says that Uvicorn is running.
4. Open:

```text
http://127.0.0.1:8010
```

Notes:

- Keep the terminal window open while using the project.
- On the first run, the script may create `.venv` and install dependencies automatically.
- Python 3.11+ must be installed on the machine.

## Manual Run

If you prefer to run it from a terminal:

```bash
cd phase2
python -m uvicorn main:app --reload
```

If your system uses `python3`:

```bash
cd phase2
python3 -m uvicorn main:app --reload
```

## Access URLs

If started with `run_local.bat`:

- Frontend UI: `http://127.0.0.1:8010`
- Swagger Docs: `http://127.0.0.1:8010/docs`

If started manually with `uvicorn` default settings:

- Frontend UI: `http://127.0.0.1:8000`
- Swagger Docs: `http://127.0.0.1:8000/docs`

## API Endpoints

- `GET /campaigns`
- `GET /campaigns/{campaign_id}`
- `POST /campaigns`
- `PUT /campaigns/{campaign_id}`
- `DELETE /campaigns/{campaign_id}`
- `GET /health`

## Project Structure

```text
phase2/
  main.py
  routers.py
  services.py
  schemas.py
  repository.py
  models.py
  database.py
  data/
    promocatch.db
  static/
    index.html
  docs/
    SAD_Phase1.md
    SAD_Phase1.pdf
    SAD_Phase2.md
    SAD_Phase2.pdf
    PromoCatch_Project_Explanation_Presentation.pptx
    screenshots/
  scripts/
    build_sad_phase2_pdf.py
    build_phase2_local_presentation.py
  Dockerfile
  docker-compose.yml
  requirements.txt
  run_local.bat
  README.md
```

## Docker Run

You can also run the project with Docker:

```bash
docker compose up --build
```

Then open:

```text
http://127.0.0.1:8000
```

## Submission Scope

This phase contains:

- SAD V1 and SAD V2 based on the 4+1 model
- Full implementation of the selected system
- Local presentation files
- Deployment-ready project files
