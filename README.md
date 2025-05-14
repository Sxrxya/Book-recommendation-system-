# Book Recommendation System using AI

This project is a basic AI-powered book recommendation system developed using Python and Google Colab. It recommends similar books based on the author's name and genre using content-based filtering (TF-IDF + cosine similarity). This is my first public AI product, aimed at solving a real-world problem with simple yet effective ML logic.

---

## Overview

This system allows users to input a book title, and the model will return a list of similar books. It uses NLP techniques to convert textual metadata like author names and genres into vectors and compares them using cosine similarity.

---

## Features
- Suggests top 5 similar books instantly
- Works fully on Google Colab and mobile Python apps like Pydroid or Kaggle
- Dataset is easy to use and public
- Beginner-friendly code with practical value

---

## Tech Stack
- **Language**: Python  
- **Libraries**: Pandas, Scikit-learn (TF-IDF, Cosine Similarity)  
- **Platform**: Google Colab / Pydroid / Kaggle

---

## Dataset Information

We used the **Goodreads Books Dataset**, which contains over 23,000 books and their metadata. Key features used:
- `title`
- `authors`
- `genres` (if available)
- `average_rating`

**Dataset Source**:  
[Kaggle - Goodreads Books Dataset](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks)

**File Used**:  
`books.csv`

**Note**: If `genres` column is missing, the model can still work using only author + title.

---

## How to Run the Project

1. Download the dataset CSV file from Kaggle.
2. Upload it into your Colab project or mobile app like Pydroid.
3. Open and run the Colab notebook: `book_recommender.ipynb`.
4. When prompted, enter the name of a book (e.g., *The Hobbit*).
5. Get 5 recommended books instantly.

---

## Example Input & Output

**Input**:  
`The Hobbit`

**Output**:
- The Fellowship of the Ring  
- The Two Towers  
- The Return of the King  
- Eragon  
- Harry Potter and the Sorcerer’s Stone  

---

## File Structure
