import os
import json
import ollama
import streamlit as st

st.title("Medical AI Chatbot")
st.write("Ask questions about patient records")

patient_data = ""

for file in os.listdir():
    if file.startswith("patient_") and file.endswith(".json"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                patient_data += json.dumps(data, indent=2) + "\n"
        except:
            st.write(f"Skipping invalid file: {file}")

question = st.text_input("Ask a question")

if question:

    prompt = f"""
You are a medical assistant chatbot.

IMPORTANT RULES:
- Answer ONLY using the patient records below.
- Do NOT use external medical knowledge.
- If the answer is not found in the records, reply: "Information not available in patient records."

Patient Records:
{patient_data}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    st.subheader("Answer")
    st.write(response["message"]["content"])