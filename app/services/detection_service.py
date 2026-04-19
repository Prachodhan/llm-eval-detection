from app.models.detector import TransformerDetector

detector = TransformerDetector()

def detect_text(text: str):
    if not text.strip():
        raise ValueError("Empty text is not allowed")

    return detector.predict(text)