# Semantic Book Recommender

This project is a semantic book recommender system powered by large language models and vector search. It allows users to get book recommendations based on natural language queries, filter by category, and sort by emotional tone using a web interface built with Gradio.

## Features

- **Semantic Search:** Find books similar to a user query using sentence embeddings and vector search.
- **Category Filtering:** Filter recommendations by book category (e.g., fiction, non-fiction).
- **Emotion Sorting:** Sort recommendations by emotional tone (e.g., joy, sadness, suspense).
- **Interactive Dashboard:** User-friendly Gradio web app for exploring recommendations.

## Project Structure

- `main.py` — Script for basic semantic search and testing in the terminal.
- `gradio-dashboard.py` — Main Gradio web app for interactive recommendations.
- `books_with_emotions.csv` — Book data with emotion and category columns.
- `books_cleaned.csv` — Cleaned book data.
- `tagged_descriptions.txt` — Preprocessed book descriptions for vector search.
- `cover-not-found.jpg` — Default image for missing book covers.
- `data-exploration.ipynb` — Notebook for downloading and exploring the dataset.
- `.venv/` — Python virtual environment (recommended for dependency management).
- `pyproject.toml` — Project metadata and dependencies.
- `README.md` — Project documentation.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Project1
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
# On Windows PowerShell:
.venv\Scripts\Activate.ps1
# On Windows CMD:
.venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
# OR, if you use pyproject.toml:
pip install -e .
```
If you do not have a `requirements.txt`, install the main dependencies:
```bash
pip install gradio pandas numpy python-dotenv sentence-transformers langchain chromadb kagglehub matplotlib seaborn ipywidgets
```

### 4. Prepare Data

- Download the dataset using `data-exploration.ipynb` (requires a Kaggle account and API key).
- Ensure `books_with_emotions.csv` and `tagged_descriptions.txt` are present in the directory.

### 5. Run the Dashboard

```bash
python gradio-dashboard.py
```
Open the local URL (e.g., http://127.0.0.1:7860/) in your browser to use the app.

## Usage

- Enter a natural language description of the kind of book you want.
- Optionally, select a category and/or emotional tone.
- View recommended books with cover images and short descriptions.

## Data Sources

- The book dataset can be downloaded from [Kaggle: 7k Books with Metadata](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata).

## Credits

- Inspired by the [freeCodeCamp tutorial and repo](https://github.com/t-redactyl/llm-semantic-book-recommender).

---

**Note:**  
If you encounter any issues with dependencies or file loading, ensure your virtual environment is activated and all required files are present in the `Project1` directory.
