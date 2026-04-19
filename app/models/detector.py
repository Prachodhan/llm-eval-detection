class SimpleDetector:
    def predict(self, text: str):
        score = min(len(text) / 500, 1.0)
        label = "AI" if score > 0.5 else "Human"

        return {
            "label": label,
            "confidence": round(score, 2)
        }