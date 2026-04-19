import torch
from app.models.model_loader import ModelLoader

class TransformerDetector:
    def __init__(self):
        self.tokenizer, self.model = ModelLoader.load()

    def predict(self, text: str):
        inputs = self.tokenizer(
            text[:512],
            return_tensors="pt",
            truncation=True,
            padding=True
        )

        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=1)

        score = probs[0][1].item()
        label = "AI" if score > 0.5 else "Human"

        return {
            "label": label,
            "confidence": round(score, 2)
        }