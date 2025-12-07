# Development of RAG-based AI system - Dalila Turashbekova

## Overview

This project is a Retrieval-Augmented Generation (RAG) cooking assistant that answers user questions about recipes and cooking tips, using **only a local dataset**.  
The goal of the task is to demonstrate how to combine an LLM with a vector database, embeddings, and a knowledge base.

Users can ask cooking-related questions such as:

- "How to cook pasta al dente?"
- "Give me a simple chicken recipe."
- "Any ideas for breakfast?"

The system retrieves relevant text chunks from the dataset and generates an answer based on the retrieved information.

---

## 1. Main Idea

Build a lightweight AI assistant that uses RAG to enhance LLM responses by retrieving helpful information from a local dataset.  
The model does not rely on general model knowledge – only on documents from `./data`.

---

## 2. Dataset Concept
Location: `./data`  
Files used:
- `recipes_easy.md`
- `cooking_tips.md`

Content: short recipes + cooking tips.  
Text is split into chunks and stored in a vector database.

---

## 3. Concepts
- Local markdown dataset → embeddings
- ChromaDB used for similarity search
- OpenAI embeddings model `text-embedding-3-small`
- LLM uses retrieved chunks as context → final answer
- Interface via CLI + Streamlit

---

## 4. System Architecture

Markdown Files → embed_data.py → Embeddings → ChromaDB → Retrieval → LLM → Final Answer

---

## 5. Technical Details

Tech stack:
- Python 3.9+
- OpenAI API
- Embeddings: `text-embedding-3-small`
- Vector DB: ChromaDB
- UI: Streamlit (`app.py`)

Key scripts:
- `src/embed_data.py` – create and store embeddings
- `src/rag_chat.py` – retrieval + answer generation
- `app.py` – web UI

Secrets stored in `.env` (not pushed to repo).

---

## 6. Requirements

- Python 3.9
- Internet for embeddings & LLM calls
- Install dependencies: `pip install -r requirements.txt`
- Add `.env` with `OPENAI_API_KEY`  

---

## 7. Limitations

- Dataset is intentionally small - limited knowledge scope  
- Internet required for LLM/Embeddings  
- No memory/history, single-turn chat  
- System provides general cooking advice (not dietary/medical)

---

## 8. How to Run

pip install -r requirements.txt         # install deps
python -m src.embed_data                # generate embeddings
streamlit run app.py                    # run UI

Optional CLI:

python -m src.rag_chat

---

## 9. GitHub Repository

🔗 https://github.com/Dali098/rag-recipe-assistant

---

## 10. Video

Video demonstration link:
(https://drive.google.com/drive/folders/1QNDMS_Ikoz2kkjbfkcXq-rGall5q5jVQ?usp=sharing)

---

## Conclusion

This project implements a complete RAG pipeline using a small recipe dataset, embeddings, ChromaDB, and an LLM.
All steps are completed according to task requirements, including dataset preparation, embedding generation, retrieval logic, UI application, and demonstration video.