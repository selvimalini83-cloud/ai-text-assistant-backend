🧠 AI Text Assistant
📌 Project Overview

AI Text Assistant is a web-based application designed to improve text quality and detect spam messages using Artificial Intelligence and Machine Learning techniques. The application provides real-time text analysis by integrating trained machine learning models and transformer-based NLP models.

This project demonstrates full-stack development skills, API integration, AI model deployment, and performance optimization techniques.

🚀 Features
✅ Spam Detection

Detects whether a message is spam or legitimate.

Uses a trained machine learning classification model.

Provides instant prediction results.

✅ Grammar Correction

Automatically corrects grammatical errors in user input.

Uses transformer-based Natural Language Processing.

Generates human-like corrected sentences.

📸 Screenshots

![alt text](image-1.png)

Spam Detection Output

![alt text](image.png)

Grammar Correction Output

(Add screenshot of grammar correction result)

🛠️ Tech Stack
Frontend

HTML

CSS

JavaScript

Hosted on Vercel

Backend

Python

Flask

Flask-CORS

Pandas

Pickle

Hugging Face Transformers

Deployment

Backend: Render

Frontend: Vercel

🤖 AI Models / APIs Used
🔹 Spam Detection Model

Traditional Machine Learning Classification Model

Trained using SMS Spam Collection Dataset

Uses Text Vectorization techniques

Model and vectorizer stored using Pickle for fast loading

🔹 Grammar Correction Model

Transformer-based NLP model

Implemented using Hugging Face Pipeline

Model Used:

prithivida/grammar_error_correcter_v1


Supports automatic grammar error correction

Uses lazy loading to optimize performance

⚙️ Performance Optimization

Grammar correction model loads only when first requested.

Separate model storage for modular design.

Cross-Origin Resource Sharing (CORS) configured for secure frontend-backend communication.

Efficient vectorization used for faster spam prediction.

🔌 API Endpoints
POST → Spam Prediction

Endpoint:

/predict-spam


Request:

{
  "text": "Congratulations! You won a prize"
}


Response:

{
  "prediction": "Spam 🚫"
}

POST → Grammar Correction

Endpoint:

/grammar


Request:

{
  "text": "I are learning AI"
}


Response:

{
  "corrected_text": "I am learning AI"
}

💻 Setup Instructions
1️⃣ Clone Repository
git clone <your-backend-repo-link>
cd <repo-folder>

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Backend Server
python app.py


Server will start on:

http://localhost:5000

4️⃣ Run Frontend

Open frontend project

Deploy using Vercel OR run locally

🌐 Deployed Application

Frontend:
👉 https://ai-text-assistant-client.vercel.app

Backend:
👉 https://ai-text-assistant-backend.onrender.com

📂 Project Structure
AI Text Assistant
│
├── ml_models
│   ├── spam
│   └── grammar
│
├── app.py
├── requirements.txt
├── README.md
└── frontend

🔮 Future Improvements

Add sentiment analysis feature

Add text summarization module

Improve grammar correction accuracy

Add user authentication system

Convert application into full AI writing assistant platform

👩‍💻 Author

Selvi Malini
BCA Graduate | Aspiring Full Stack & AI Developer

⭐ Skills Demonstrated

Full Stack Development

Machine Learning Integration

NLP Model Deployment

REST API Development

Cloud Deployment (Render & Vercel)

Performance Optimization
