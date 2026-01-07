from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import torch

app = Flask(__name__)
CORS(app)

# ===== Load Spam Model =====
with open("ml_models/spam/spam_model.pkl", "rb") as f:
    spam_model = pickle.load(f)

with open("ml_models/spam/vectorizer.pkl", "rb") as f:
    spam_vectorizer = pickle.load(f)
# for grammar
from transformers import pipeline

grammar_corrector = pipeline(
    "text2text-generation",
    model="prithivida/grammar_error_correcter_v1",
    tokenizer="prithivida/grammar_error_correcter_v1"
)

# Load grammar data
grammar_df = pd.read_csv("ml_models/grammar/grammar_dataset.csv")

# Load vectorizer
with open("ml_models/grammar/grammar_vectorizer.pkl", "rb") as f:
    grammar_vectorizer = pickle.load(f)

# Load NearestNeighbors model
with open("ml_models/grammar/grammar_model.pkl", "rb") as f:
    grammar_model = pickle.load(f)

# ===== Serve Frontend Files =====
@app.route("/")
def index():
    return send_from_directory("frontend", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("frontend", path)

# ===== Spam Prediction API =====
@app.route("/predict-spam", methods=["POST"])
def predict_spam():
    data = request.get_json()
    text = data.get("text", "")

    if text.strip() == "":
        return jsonify({"prediction": "Please enter text ⚠️"})

    vector = spam_vectorizer.transform([text])
    result = spam_model.predict(vector)[0]

    prediction = "Spam 🚫" if int(result) == 1 else "Not Spam ✅"
    return jsonify({"prediction": prediction})


# -------- GRAMMAR API --------
@app.route("/grammar", methods=["POST"])
def grammar_predict():
    data = request.get_json()
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"corrected_text": "⚠️ Please enter text"})

    # 👉 If you are using TRANSFORMERS grammar corrector
    result = grammar_corrector(text, max_new_tokens=64)

    corrected = result[0]["generated_text"]

    return jsonify({
        "corrected_text": corrected
    })



if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

