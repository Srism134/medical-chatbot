import ollama
import json
import os

patient_data = ""

for file in os.listdir():
    if file.startswith("patient_") and file.endswith(".json"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                patient_data += json.dumps(data, indent=2) + "\n"
        except Exception as e:
            print(f"Skipping invalid file: {file}")

print("Medical Chatbot Ready!")
print("Ask a question about the patients.\n")

while True:
    question = input("You: ")

    prompt = f"""
You are a medical assistant.

Use the following patient records to answer the question.

Patient Records:
{patient_data}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    print("Bot:", response["message"]["content"])