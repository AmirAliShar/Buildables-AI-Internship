🧠 AI Text Generation App

This project is a simple AI-powered text generation application built with FastAPI (backend) and Streamlit (frontend). It allows users to input text and receive responses in different writing styles such as:

📄 News Article

🎓 Academic Abstract

📱 Social Media Post

⚙️ Technical Documentation

✍️ Creative Writing

🚀 Features

FastAPI Backend – Handles requests, calls the LLM, and returns structured responses.

Streamlit Frontend – Simple and interactive UI for testing.

LLM Token & Cost Info – Get tokens used and approximate cost for generation.

Environment Variables – API keys are stored securely with .env.

🛠️ Installation

Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-na

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

Install dependencies 
pip install -r requirements.txt


⚙️ Setup

Create a .env file in the project root.

Add your API key:

GROQ_API_KEY

▶️ Run the App
Start Backend (FastAPI)

uvicorn backend.main:app --reload

Start Frontend (Streamlit)
streamlit run frontend/app.py


📂 Project Structure

week01
├── README.md
├── main.py
├── requirements.txt
├── config.py
├── utils/
│   ├── __init__.py
│   ├── llm_helpers.py
└   ── Schema.py
│   └── tokenizer_helpers.py
├── data/
│   ├── sample_texts/
│   └── results/
├── tests/
│   └── test_main.py 
    └── test_main.py
└── docs/
    └── usage_examples.md


🧪 Usage Example

  "Write a short social media post about AI in education."
  
Resposne
{
  "text": "AI is transforming classrooms worldwide...",
  "response": "Social Media Post",
  "llm_name": "groq/llm",
  "tokens": 142,
  "cost": 0.0012
}
