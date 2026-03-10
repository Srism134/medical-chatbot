import ollama
import json
import os

# store all patient data
patient_data = ""

# read all patient JSON files
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

# chatbot loop
while True:
    question = input("You: ")

    prompt = f"""
You are a medical assistant chatbot.

IMPORTANT RULES:
- Answer ONLY using the patient records below.
- Do NOT use external medical knowledge.
- If the answer is not found in the records, reply: "Information not available in patient records."

Patient Records:
{patient_data}

User Question:
{question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("\nBot:", response["message"]["content"])