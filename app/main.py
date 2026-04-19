from fastapi import FastAPI
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.detect import router as detect_router


app = FastAPI(title="LLM Eval Detection")

app.include_router(health_router, prefix="/v1")

app.include_router(detect_router, prefix="/v1")