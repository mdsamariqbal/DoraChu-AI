DoraChu – Multi-Agent AI Decision System

DoraChu is a FastAPI-based multi-agent AI system that analyzes user problems from multiple perspectives and generates a balanced final recommendation using local LLMs (Ollama).

Features
	•	Multi-agent architecture (Emotional, Logical, Career, Motivation, Planning)
	•	Decision Agent that combines all responses
	•	REST API built with FastAPI
	•	Local LLM inference using Ollama (Phi3/Llama3)
	•	Modular and extensible design

Tech Stack

Python, FastAPI, Pydantic, Ollama, REST API

How to Run
	1.	Clone the repository
git clone https://github.com/mdsamariqbal/DoraChu-AI.git
cd DoraChu-AI
	2.	Install dependencies
pip install -r requirements.txt
	3.	Pull and run model
ollama pull phi3
	4.	Start the server
uvicorn main2:app –reload

Open: http://127.0.0.1:8000/docs

API

POST /solve
Input:
{ “problem”: “I am confused about my career” }

Use Cases

Career guidance, study planning, stress management, AI decision support.
