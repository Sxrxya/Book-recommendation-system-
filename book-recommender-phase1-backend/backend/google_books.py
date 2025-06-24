import requests

def fetch_books(query, max_results=10):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}"
    response = requests.get(url)
    data = response.json()
    books = []

    for item in data.get("items", []):
        info = item.get("volumeInfo", {})
        books.append({
            "title": info.get("title", "N/A"),
            "authors": info.get("authors", ["N/A"]),
            "description": info.get("description", ""),
        })
    return books