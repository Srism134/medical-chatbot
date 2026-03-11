\# Medical AI Chatbot



!\[Medical Chatbot Demo](medical\_chatbot\_demo.png)



\## Overview



This project is an AI-powered medical assistant that answers questions based on patient medical records using a local Large Language Model (LLM).



The chatbot processes patient JSON records and generates responses using a local LLM running through Ollama.



---



\## Demo Video



Watch the chatbot demo in the repository video file:



medical\_chatbot\_demo.mp4



---



\## Features



\- Local LLM using Ollama (Llama3)

\- Patient medical record analysis

\- JSON medical dataset processing

\- Prompt-controlled responses (prevents hallucinations)

\- Retrieval-Augmented Generation (RAG)

\- Chatbot conversation memory

\- Web chatbot interface using Streamlit



---



\## Project Structure



medical-chatbot

│

├── app.py

├── rag\_chatbot.py

├── test\_llm.py

├── requirements.txt

├── medical\_chatbot\_demo.mp4

├── medical\_chatbot\_demo.png

├── README.md

├── .gitignore

├── data/

└── embeddings/



---



\## Technologies Used



\- Python

\- Ollama

\- Llama3

\- Streamlit

\- FAISS

\- Sentence Transformers

\- NumPy



---



\## Installation



Clone the repository:



git clone https://github.com/Srism134/medical-chatbot.git



Go to the project folder:



cd medical-chatbot



Install dependencies:



pip install -r requirements.txt



Make sure Ollama is installed and the Llama3 model is downloaded.



---



\## Run the Chatbot



Basic chatbot:



python test\_llm.py



RAG chatbot:



python rag\_chatbot.py



Web chatbot interface:



streamlit run app.py



---



\## Example Questions



\- Which patient has diabetes?

\- What medications are patients taking?

\- Which patient visited most recently?



---



\## Important Note



The chatbot answers \*\*only using the patient records provided in the dataset\*\* and does not generate external medical advice.



---



\## Author



Smriti  

MSc Data Science  

Northumbria University

