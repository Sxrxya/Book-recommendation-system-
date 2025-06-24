# Book Recommendation System using AI
# 📚 AI Book Recommender System

This is a full-stack AI-powered Book Recommendation System built using **Sentence-BERT**, **Faiss**, **Flask**, and **React**. It integrates the Google Books API to fetch real-time data and provides semantic search recommendations based on user input.

---

## 🚀 Features

- 🔍 Semantic book search using Sentence-BERT + Faiss
- 📚 Real-time book info via Google Books API
- 🧠 AI backend built with Flask
- 🌐 Modern frontend built with React
- ⚡ Fast local deployment and GitHub-ready

---

## 🧠 Tech Stack

| Layer    | Tech                 |
|----------|----------------------|
| Backend  | Python, Flask, Faiss, Sentence-Transformers |
| Frontend | React, HTML, CSS     |
| API      | Google Books API     |

---

## 📁 Project Structure

book-recommender/
├── backend/ # Flask API
│ ├── app.py
│ ├── index_faiss.py
│ ├── google_books.py
│ ├── embedder.py
│ └── requirements.txt
├── frontend/ # React App
│ ├── public/
│ └── src/
├── .gitignore
└── README.md


## 🧪 How to Run

### 🖥 Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
It will run at: http://127.0.0.1:5000

🌐 Frontend
cd frontend
npm install
npm start
It will run at: http://localhost:3000

🔗 API Endpoint
GET /recommend?q=search_term
Example:
http://127.0.0.1:5000/recommend?q=atomic%20habits
🙌 Built by
Suriyaprakash M
AI & Data Science Student 
