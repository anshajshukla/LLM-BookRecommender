import os
import pandas as pd
from dotenv import load_dotenv

# LangChain & Embedding
from sentence_transformers import SentenceTransformer
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Load environment variables
load_dotenv()
hugging_face_key = os.getenv("HUGGINGFACE_API_KEY")

# Load SentenceTransformer model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load and preprocess book data
books = pd.read_csv("books_cleaned.csv")

# Save tagged descriptions to file (ensure this column exists)
books["tagged_description"].to_csv("tagged_descriptions.txt", sep="\n", index=False, header=False)

# Load documents
raw_documents = TextLoader("tagged_descriptions.txt",encoding="utf-8").load()

# Split text into chunks
text_splitter = CharacterTextSplitter(chunk_size=0, chunk_overlap=0, separator="\n")
documents = text_splitter.split_documents(raw_documents)

# Create Chroma vector database
db_books = Chroma.from_documents(documents, embedding_model)

# Semantic search function
def retrieve_semantic_recommendations(query: str, top_k: int = 10) -> pd.DataFrame:
    recommendations = db_books.similarity_search(query, k=50)
    isbn_list = []
    for doc in recommendations:
        isbn_str = doc.page_content.split()[0].strip().strip('"')
        try:
            isbn_list.append(int(isbn_str))
        except ValueError:
            print(f"Could not convert '{isbn_str}' to an integer. Skipping.")
            continue
    return books[books["isbn13"].isin(isbn_list)].head(top_k)


if __name__ == "__main__":
   q = input("Enter you query: ")
   recs = retrieve_semantic_recommendations(q)
   print(recs)
