from app.models.detector import SimpleDetector

detector = SimpleDetector()

def detect_text(text: str):
    return detector.predict(text)