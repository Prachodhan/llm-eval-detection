from pydantic import BaseModel

class DetectionResponse(BaseModel):
    label: str
    confidence: float