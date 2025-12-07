# RAG Recipe Assistant

## 1. Main Idea
A small RAG-based assistant that answers cooking questions using only information stored in a local dataset of recipes and cooking tips.  
The goal is to demonstrate how documents + embeddings + vector search + LLM can work together in a simple AI tool.

---

## 2. Concepts
- Local text data: transformed into embeddings
- Vector search used to find relevant content
- Retrieved context + user question: passed to LLM
- Model answers based only on provided knowledge (no external data)

---

## 3. Dataset Concept
Location: `./data/`  
Format: Markdown `.md` files

Included files:
- `recipes_easy.md` - short simple recipes
- `cooking_tips.md` - helpful cooking tricks and instructions

Text is split into chunks and converted into embeddings.  
Dataset is small but representative enough for retrieval testing.

---

## 4. Design Details
Architecture consists of two stages:

### Offline (data preparation)
1. Read `.md` files
2. Split text into chunks
3. Generate embeddings with `text-embedding-3-small`
4. Save documents + vectors in ChromaDB

### Online (question answering)
1. User asks question through CLI or Streamlit UI
2. System embeds query: finds similar chunks
3. Builds prompt using retrieved documents
4. LLM generates final grounded answer

---

## 5. System Technical Details
- **Language:** Python
- **Embeddings:** `text-embedding-3-small`
- **Vector DB:** ChromaDB (`PersistentClient`)
- **LLM model:** `gpt-4.1-mini`
- **UI options:** CLI and Streamlit web app
- **Secrets stored in:** `.env`

Run:

python -m src.embed_data     # generate embeddings
streamlit run app.py         # launch UI
# or
python -m src.rag_chat       # CLI chat mode

---

## 6. Requirements

- Python
- Virtual environment (venv)
- OpenAI API key in `.env`
- Internet connection for embeddings & LLM requests
- Local dataset stored in `./data`

---

## 7. Limitations

- Small dataset: answers limited to provided recipes and tips
- English-only responses
- No memory or chat history
- Retrieval quality depends on chunking and embeddings
- Not intended for professional dietary or medical advice

---

## 8. Video link:
https://drive.google.com/drive/folders/1QNDMS_Ikoz2kkjbfkcXq-rGall5q5jVQ?usp=sharing

