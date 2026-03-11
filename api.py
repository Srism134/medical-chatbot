from fastapi import FastAPI
from pydantic import BaseModel
import json
import os
import ollama

app = FastAPI()

# Load patient records
patients = {}

for file in os.listdir():
    if file.startswith("patient_") and file.endswith(".json"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
                patients[file.replace(".json", "")] = content
        except Exception as e:
            print("Skipping file:", file)


class QueryRequest(BaseModel):
    mrd_number: str
    query: str


@app.post("/query")
def query_patient(request: QueryRequest):

    if request.mrd_number not in patients:
        return {
            "error": "Invalid MRD number"
        }

    if not request.query.strip():
        return {
            "error": "Query cannot be empty"
        }

    patient_data = patients[request.mrd_number]

    prompt = f"""
You are a medical assistant chatbot.

IMPORTANT RULES:
- Answer ONLY using the patient record below
- No external knowledge
- If answer not present say "Information not available in patient record"

Patient Record:
{patient_data}

Question:
{request.query}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "mrd_number": request.mrd_number,
        "answer": response["message"]["content"],
        "confidence": "Medium"
    }