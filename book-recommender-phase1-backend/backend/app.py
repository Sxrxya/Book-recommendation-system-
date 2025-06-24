from flask import Flask, request, jsonify
from google_books import fetch_books
from index_faiss import BookSearchEngine

app = Flask(__name__)

# Initial load
initial_books = fetch_books("popular books 2024")
engine = BookSearchEngine(initial_books)

@app.route("/recommend", methods=["GET"])
def recommend():
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "Query required"}), 400

    results = engine.search(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
