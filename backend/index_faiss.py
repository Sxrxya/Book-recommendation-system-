import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from google_books import fetch_books

class BookSearchEngine:
    def __init__(self, books):
        self.books = books
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.embeddings = self.encode_books()
        self.index.add(self.embeddings)

    def encode_books(self):
        texts = [f"{book['title']} {book['authors']}" for book in self.books]
        return self.model.encode(texts)

    def search(self, query, k=5):
        query_vec = self.model.encode([query])
        _, I = self.index.search(np.array(query_vec), k)
        return [self.books[i] for i in I[0]]
