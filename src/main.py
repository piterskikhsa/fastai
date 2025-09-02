from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def create_app():
    _app = FastAPI(
        title="FastAI",
        version="0.1.0",
        description="AI-powered website generator backend for FastAI",
    )

    # Для статических файлов (CSS, JS, изображения)
    _app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")
    # Для HTML-страниц с автоматическим index.html
    _app.mount("/", StaticFiles(directory="static", html=True), name="static")

    return _app


app = create_app()
