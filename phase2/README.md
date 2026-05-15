# PromoCatch - Campaign and Deal Tracking System (Phase 2)

PromoCatch is a Software Architecture Project implemented as a **Layered REST API**. In Phase 2, the system supports full campaign management: listing, searching, filtering, creating, updating, and deleting campaigns through a complete web interface.

## Architecture

The project follows a strict layered architecture:

- **Presentation Layer**: `static/index.html`
- **Control Layer**: `main.py`, `routers.py`
- **Domain Layer**: `schemas.py`, `services.py`
- **Resource Layer**: `database.py`, `models.py`, `repository.py`

## Technology Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- HTML, CSS, Bootstrap
- Vanilla JavaScript

## Prerequisites

Install Python 3.11 or newer.

You can check your Python version with:

```bash
python --version
```

On some systems, the command may be:

```bash
python3 --version
```

## Installation

Open a terminal in the project folder and install the dependencies:

```bash
pip install -r requirements.txt
```

If your system uses `python3`, use:

```bash
python3 -m pip install -r requirements.txt
```

## Running the Application (Local)

Start the FastAPI server with:

```bash
python -m uvicorn main:app --reload
```

Alternative command:

```bash
python3 -m uvicorn main:app --reload
```

## Access URLs

Frontend UI:

```text
http://127.0.0.1:8000
```

Swagger API Documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

- `GET /campaigns`: Lists campaigns (supports `q`, `platform`, `min_discount`, `max_discount` query params).
- `GET /campaigns/{campaign_id}`: Returns campaign detail.
- `POST /campaigns`: Adds a new campaign.
- `PUT /campaigns/{campaign_id}`: Updates an existing campaign.
- `DELETE /campaigns/{campaign_id}`: Deletes a campaign.
- `GET /health`: Health check endpoint for deployment validation.

## Project Structure

```text
Phase2_SAD_Code_CemilTekin_KaanKesen_OmerTaricandir/
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
    PromoCatch_Project_Explanation_Presentation.pptx
    SAD_Phase1.md
    SAD_Phase1.pdf
    SAD_Phase2.md
    SAD_Phase2.pdf
    screenshots/
  scripts/
    build_sad_phase2_pdf.py
    build_phase2_local_presentation.py
  Dockerfile
  docker-compose.yml
  requirements.txt
  README.md
```

## Running with Docker

Build and run with Docker Compose:

```bash
docker compose up --build
```

Then open:

```text
http://127.0.0.1:8000
```

## Phase 2 Scope

This submission includes:

- Software Architecture Document V1 and V2 using 4+1 views.
- English project explanation presentation with local application screenshots.
- Complete frontend implementation for campaign management.
- Complete backend implementation using FastAPI (CRUD + filters).
- SQLite database persistence.
- Docker-based deployment configuration (`Dockerfile`, `docker-compose.yml`).
- Layered architecture separation across presentation, control, domain, and resource layers.
