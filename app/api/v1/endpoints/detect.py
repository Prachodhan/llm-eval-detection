from fastapi import APIRouter
from app.schemas.request import TextRequest
from app.schemas.response import DetectionResponse
from app.services.detection_service import detect_text

router = APIRouter()

@router.post("/detect", response_model=DetectionResponse)
def detect(req: TextRequest):
    return detect_text(req.text)