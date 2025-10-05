# 🧠 Retrieval-Augmented Generation (RAG) from PDF

This project implements a **Retrieval-Augmented Generation (RAG)** system that can intelligently answer user questions based on the contents of uploaded **PDF documents**.  
It combines **PDF text extraction**, **semantic chunking**, **vector storage**, and **LLM-based retrieval** to generate accurate, context-grounded answers.


## 🚀 Features

✅ Extract text from PDFs using multiple methods  
✅ Chunk and embed text into a vector database (Chroma)  
✅ Retrieve top relevant passages for any user query  
✅ Compare RAG vs Non-RAG (direct LLM) answers  
✅ Analyze when RAG improves response quality  
✅ Simple and reproducible setup (Python + LangChain)

## 🧩 System Overview

plaintext
PDF → Text Extraction → Chunking → Embedding → Chroma Vector Store
        ↑                                         ↓
      User Question  →  Retrieve Relevant Chunks  →  LLM Answer


# 🛠️ Setup Instructions
1. Clone this repository

# 2. Create and activate environment

python -m venv venv
venv\Scripts\activate   # (Windows)
# or
source venv/bin/activate  # (Mac/Linux)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables

Create a .env file in the root folder:
GROQ_API_KEY=your_groq_api_key

# 📦 Libraries Used
| Category       | Libraries                                                                  |
| -------------- | -------------------------------------------------------------------------- |
| PDF Processing | `langchain_community.document_loaders.PyPDFLoader`                         |
| Text Splitting | `RecursiveCharacterTextSplitter`                                           |
| Vector DB      | `Chroma`                                                                   |
| Embeddings     | `OllamaEmbeddings`                                                         |
| LLM            | `ChatGroq` (via `langchain_groq`)                                          |
| Framework      | `LangChain`                                                                |
| Utility        | `dotenv`                                                                   |


# 🧰 Challenges & Solutions
Challenge	Solution
FAISS not supported on Windows	Switched to Chroma
Some PDFs missing text	Used  PyPDFLoader
Context truncation	Adjusted chunk size & overlap
Low retrieval accuracy	Used better embedding model (nomic-embed-text)
