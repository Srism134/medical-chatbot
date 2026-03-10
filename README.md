# \# Medical AI Chatbot

# 

# !\[Medical Chatbot Demo](medical\_chatbot\_demo.png)

# Medical AI Chatbot

This project is an AI-powered medical assistant that answers questions based on patient medical records using a local Large Language Model.

## Features

* Local LLM using Ollama (Llama3)
* Patient medical record analysis
* JSON medical dataset processing
* Prompt-controlled responses (prevents hallucinations)
* Optional RAG architecture for scalable retrieval
* Web chatbot interface using Streamlit

## Project Structure

medical-chatbot
│
├── app.py                # Streamlit web chatbot
├── rag\_chatbot.py        # RAG-based chatbot
├── test\_llm.py           # Basic chatbot
├── patients.txt          # Sample dataset
├── data/                 # Patient records
├── embeddings/           # Vector embeddings
├── README.md
└── .gitignore

## Technologies Used

* Python
* Ollama
* Llama3
* Streamlit
* FAISS
* Sentence Transformers

## \## Installation

## 

## Clone the repository:

## 

## git clone https://github.com/Srism134/medical-chatbot.git

## 

## Go to the project folder:

## 

## cd medical-chatbot

## 

## Install dependencies:

## 

## pip install -r requirements.txtRun the Chatbot

Basic version:

python test\_llm.py

RAG version:

python rag\_chatbot.py

Web interface:

streamlit run app.py

## Example Questions

* Which patient has diabetes?
* What medications are patients taking?
* Which patient visited most recently?

## Important Note

The chatbot only answers using the provided patient records and does not generate external medical advice.

## Author

Smriti

