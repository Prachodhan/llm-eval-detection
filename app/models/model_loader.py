from transformers import AutoTokenizer, AutoModelForSequenceClassification

class ModelLoader:
    _model = None
    _tokenizer = None

    @classmethod
    def load(cls):
        if cls._model is None:
            cls._tokenizer = AutoTokenizer.from_pretrained(
                "distilbert-base-uncased-finetuned-sst-2-english"
            )
            cls._model = AutoModelForSequenceClassification.from_pretrained(
                "distilbert-base-uncased-finetuned-sst-2-english"
            )
            cls._model.eval()

        return cls._tokenizer, cls._model