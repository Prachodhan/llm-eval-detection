from fastapi import APIRouter
from app.schemas.request import TextRequest
from app.services.detection_service import detect_text

router = APIRouter()

@router.post("/detect")
def detect(req: TextRequest):
    return detect_text(req.text)