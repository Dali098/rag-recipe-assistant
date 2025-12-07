import os
from dotenv import load_dotenv

import streamlit as st
from openai import OpenAI

from src.db_config import get_or_create_collection
from src.llm_client import generate_answer

# ─── Setup ──────────────────────────────────────────────────────────────────────

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
collection = get_or_create_collection()


def embed_query(text: str):
    """Create an embedding vector for the user query."""
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=[text],
    )
    return response.data[0].embedding


def build_prompt(context_docs, user_question: str) -> str:
    """Build a single prompt that includes retrieved docs + user question."""
    context_block = "\n\n---\n\n".join(context_docs)
    return (
        "You are a friendly cooking assistant. Use ONLY the context below to help the user.\n"
        "Answer in simple English with step-by-step instructions.\n\n"
        f"Context:\n{context_block}\n\n"
        f"User question:\n{user_question}\n\n"
        "Now give a helpful answer based on the context."
    )


# ─── Streamlit UI ───────────────────────────────────────────────────────────────

st.set_page_config(page_title="RAG Recipe Assistant", page_icon="🍳")

st.title("🍳 RAG Recipe Assistant")
st.write(
    "Ask a cooking question and the assistant will answer using recipes and "
    "cooking tips from the local dataset."
)

user_question = st.text_input("Your question:", placeholder="e.g. What can I cook with chicken and potatoes?")
ask_button = st.button("Ask")

if ask_button and user_question.strip():
    with st.spinner("Thinking..."):
        query_embedding = embed_query(user_question)
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3,
        )
        context_docs = results.get("documents", [[]])[0]

        prompt = build_prompt(context_docs, user_question)

        system_prompt = (
            "You are a helpful assistant that answers cooking questions "
            "using provided recipes and cooking tips."
        )

        answer = generate_answer(system_prompt, prompt)

    st.subheader("Assistant answer")
    st.write(answer)

    # Optional: show which docs were used
    with st.expander("Show retrieved context"):
        for i, doc in enumerate(context_docs, start=1):
            st.markdown(f"**Document {i}:**")
            st.code(doc)
