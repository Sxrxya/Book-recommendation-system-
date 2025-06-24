import faiss
import numpy as np
from embedder import encode_texts


class BookSearchEngine:
    def __init__(self, books):
        self.books = books
        self.index = None
        self.embeddings = encode_texts([book["description"] for book in books])
        self._build_index()

    def _build_index(self):
        dim = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(self.embeddings))

    def search(self, query, top_k=5):
        query_embedding = encode_texts([query])[0]
        D, I = self.index.search(np.array([query_embedding]), top_k)
        return [self.books[i] for i in I[0]]