from fastapi import APIRouter
from app.schemas.request import TextRequest

router = APIRouter()

@router.post("/detect")
def detect(req: TextRequest):
    return {
        "label": "AI",
        "confidence": 0.5
    }