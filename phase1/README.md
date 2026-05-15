# PromoCatch - Campaign and Deal Tracking System (Phase 1)

PromoCatch is a Software Architecture Project implemented as a **Layered REST API**. This Phase 1 submission focuses on architecture design and initial implementation: documenting the system with SAD Version 1, providing use case/logical/process views, and delivering working frontend/backend code for the campaign tracking scenario.

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
Phase1_SAD_Code_CemilTekin_KaanKesen_OmerTaricandir/
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

## Running with Docker

Build and run with Docker Compose:

```bash
docker compose up --build
```

Then open:

```text
http://127.0.0.1:8000
```

## Phase 1 Scope

This submission includes:

- Software Architecture Document V1 using 4+1 architectural views.
- System selection, purpose, users, and main functionalities.
- Use case view with diagram and related partial UI implementation.
- Logical view with UML diagrams, component relationships, and related backend code.
- Process view with workflows, sequence diagram, and related code snippets.
- Frontend and backend implementation using a layered REST API structure.
- SQLite database persistence.
- Layered architecture separation across presentation, control, domain, and resource layers.
