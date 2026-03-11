import os
import json
import ollama
import streamlit as st

st.title("Medical AI Chatbot")
st.write("Ask questions about patient records")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Load patient data
patient_data = ""

for file in os.listdir():
    if file.startswith("patient_") and file.endswith(".json"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                patient_data += json.dumps(data, indent=2) + "\n"
        except:
            st.write(f"Skipping invalid file: {file}")

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if prompt := st.chat_input("Ask about patient records"):

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    # Create AI prompt
    full_prompt = f"""
You are a medical assistant chatbot.

IMPORTANT RULES:
- Answer ONLY using the patient records below.
- Do NOT use external medical knowledge.
- If the answer is not found, say: "Information not available in patient records."

Patient Records:
{patient_data}

Conversation:
{st.session_state.messages}

Question:
{prompt}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": full_prompt}]
    )

    answer = response["message"]["content"]

    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.write(answer)