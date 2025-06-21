import joblib


class EmailScanner:
    def __init__(self, model_path, vectorizer_path):
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def scan_text(self, email_body: str) -> bool:
        vector = self.vectorizer.transform([email_body])
        prediction = self.model.predict(vector)
        return bool(prediction[0])
