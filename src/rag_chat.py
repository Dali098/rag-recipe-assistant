import os
from dotenv import load_dotenv
from openai import OpenAI

from src.db_config import get_or_create_collection
from src.llm_client import generate_answer

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def embed_query(text: str):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=[text]
    )
    return response.data[0].embedding

def build_prompt(context_docs, user_question: str) -> str:
    context_block = "\n\n---\n\n".join(context_docs)
    return (
        "You are a friendly cooking assistant. Use ONLY the context below to help the user.\n"
        "Answer in simple English with step-by-step instructions.\n\n"
        f"Context:\n{context_block}\n\n"
        f"User question:\n{user_question}\n\n"
        "Now give a helpful answer based on the context."
    )

def chat():
    collection = get_or_create_collection()
    print("\n🍳 RAG Recipe Assistant is ready! Type a question (or 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ("exit", "quit"):
            print("Bye! 👋")
            break

        query_embedding = embed_query(user_input)

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3,
        )

        context_docs = results.get("documents", [[]])[0]

        prompt = build_prompt(context_docs, user_input)

        system_prompt = (
            "You are a helpful assistant that answers cooking questions "
            "using provided recipes and cooking tips."
        )

        answer = generate_answer(system_prompt, prompt)
        print("\nAssistant:\n", answer, "\n")

if __name__ == "__main__":
    chat()
