from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.web import router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="Kaufpreisaufteilung",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

app.include_router(router)