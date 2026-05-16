# PromoCatch - Phase 1

PromoCatch is a campaign and deal tracking system built as a layered REST API.  
Phase 1 contains the initial implementation and SAD Version 1.

## What This Phase Includes

- System selection and scope definition
- SAD V1
- Initial frontend and backend implementation
- Use case, logical, and process views
- SQLite-based persistence

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

## Prerequisites

Install Python 3.11 or newer.

## Run Locally

```bash
cd phase1
python -m uvicorn main:app --reload
```

If your system uses `python3`:

```bash
cd phase1
python3 -m uvicorn main:app --reload
```

## Access URLs

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
phase1/
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
  Dockerfile
  docker-compose.yml
  requirements.txt
  README.md
```

## Docker Run

```bash
docker compose up --build
```

Then open:

```text
http://127.0.0.1:8000
```
