from app.models.detector import SimpleDetector

detector = SimpleDetector()

def detect_text(text: str):
    if not text.strip():
        raise ValueError("Empty text is not allowed")
    
    return detector.predict(text)