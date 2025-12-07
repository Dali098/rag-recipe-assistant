# RAG Recipe Assistant

A small Retrieval-Augmented-Generation (RAG) project that answers cooking questions using a local markdown dataset of recipes.  
The system uses embeddings, ChromaDB vector search, and LLM for answer generation.

---

## Video Demo

*Project demonstration:*  
(https://drive.google.com/drive/folders/1QNDMS_Ikoz2kkjbfkcXq-rGall5q5jVQ?usp=sharing)

---

## Features

- Local dataset stored in `./data/*.md`
- Embeddings generated via `text-embedding-3-small`
- Vector search using ChromaDB
- RAG pipeline with custom prompt
- Two ways to run:
  - CLI chat mode
  - Streamlit web UI

---

## How to Run

# create environment
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# generate embeddings
python -m src.embed_data

# run UI
streamlit run app.py

---

## Tech Stack

- Python 3.9+
- OpenAI API
- ChromaDB
- Streamlit
- Embeddings + LLM

## Notes

- .env is ignored for safety — add your OPENAI_API_KEY manually
- Dataset is intentionally small for demo purposes
- Designed as an educational RAG example for beginners