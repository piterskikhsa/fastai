from fastapi import FastAPI


def create_app():
    _app = FastAPI(
        title="FastAI",
        version="0.1.0",
        description="AI-powered website generator backend for FastAI",
    )
    return _app


app = create_app()
