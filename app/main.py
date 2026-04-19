from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.models.model_loader import ModelLoader
from app.api.v1.endpoints import detect, health


@asynccontextmanager
async def lifespan(app: FastAPI):
    ModelLoader.load()
    print("Model loaded")

    yield


app = FastAPI(lifespan=lifespan)

app.include_router(detect.router, prefix="/v1")
app.include_router(health.router, prefix="/v1")