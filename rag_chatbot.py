import os
import json
import ollama
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
doc_texts = []

print("Loading patient files...")

for file in os.listdir():
    if file.startswith("patient_") and file.endswith(".json"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
                text = json.dumps(data)
                documents.append(text)
                doc_texts.append(text)
        except:
            print("Skipping invalid file:", file)

print("Creating embeddings...")

embeddings = model.encode(doc_texts)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

print("Medical RAG Chatbot Ready!\n")

while True:

    question = input("You: ")

    q_embedding = model.encode([question])

    k = 3
    distances, indices = index.search(np.array(q_embedding), k)

    context = ""

    for i in indices[0]:
        context += documents[i] + "\n"

    prompt = f"""
You are a medical assistant.

Use ONLY the information from the patient records below.

Patient Records:
{context}

Question:
{question}

If the answer is not in the records say:
Information not available in patient records.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    print("\nBot:", response["message"]["content"], "\n")