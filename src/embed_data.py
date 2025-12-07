import os
import glob
from dotenv import load_dotenv
from openai import OpenAI
from src.db_config import get_or_create_collection

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_markdown_files(folder="data"):
    texts = []
    for file in glob.glob(f"{folder}/*.md"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            # split into chunks by double newline
            chunks = [c.strip() for c in content.split("\n\n") if c.strip()]
            texts.extend(chunks)
    return texts

def embed_texts(texts):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [item.embedding for item in response.data]

def main():
    collection = get_or_create_collection()

    texts = read_markdown_files()
    print(f"Loaded {len(texts)} chunks from data folder")

    embeddings = embed_texts(texts)
    ids = [f"id_{i}" for i in range(len(texts))]
    metadatas = [{"source": "recipes"} for _ in texts]

    collection.add(
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )

    print("Embeddings generated & stored successfully!")

if __name__ == "__main__":
    main()
