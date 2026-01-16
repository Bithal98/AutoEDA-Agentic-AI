import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_data(question: str, eda_context: dict):
    """
    Chat agent that answers questions based on EDA context
    """

    prompt = f"""
You are a data analyst AI.

You are given EDA results of a dataset.
Use ONLY this information to answer the user's question clearly.

EDA CONTEXT:
{eda_context}

USER QUESTION:
{question}

Answer in simple and clear language.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
