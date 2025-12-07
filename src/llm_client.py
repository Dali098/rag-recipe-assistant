import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",   # можно поменять модель при желании
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()
