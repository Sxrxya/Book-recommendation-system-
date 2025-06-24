# AI Book Recommender – Phase 1 (Backend)

### Features:
- Google Books API Integration
- Sentence-BERT for text embeddings
- FAISS for fast semantic similarity search
- Flask API endpoint `/recommend?q=your_query`

### Setup
```bash
pip install -r requirements.txt
python backend/app.py
```

Then visit: `http://localhost:5000/recommend?q=magic school`