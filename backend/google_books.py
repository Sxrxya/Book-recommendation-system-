import requests

def fetch_books(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    response = requests.get(url)
    items = response.json().get("items", [])[:20]
    books = []
    for item in items:
        volume = item.get("volumeInfo", {})
        books.append({
            "title": volume.get("title", "No Title"),
            "authors": ", ".join(volume.get("authors", ["Unknown"]))
        })
    return books
