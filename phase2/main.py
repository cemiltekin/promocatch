from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import models  # Registers SQLAlchemy models on Base metadata.
import services
from database import Base, SessionLocal, engine
from routers import router as campaign_router


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create tables and seed demo data when the application starts."""
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        services.seed_initial_campaigns(db)
    finally:
        db.close()
    yield


app = FastAPI(
    title="PromoCatch API",
    description="Campaign and deal tracking system built with layered architecture.",
    version="2.0.0",
    lifespan=lifespan,
)

app.include_router(campaign_router)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", include_in_schema=False)
def serve_index():
    """Serve the PromoCatch web interface."""
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    """Return empty favicon response to avoid noisy 404 logs."""
    return Response(status_code=204)


@app.get("/health", tags=["Health"])
def health_check():
    """Lightweight health endpoint for deployment checks."""
    return {"status": "ok"}
