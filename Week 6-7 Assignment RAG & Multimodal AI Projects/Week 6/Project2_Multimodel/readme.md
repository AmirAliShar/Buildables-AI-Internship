# 📘 Multimodal RAG: Long-Context Document Q&A System  

## 🧩 Project Overview  
This project implements a **Multimodal Retrieval-Augmented Generation (RAG) System** capable of analyzing and understanding **PDF documents containing text, tables, and charts**.  

It uses **Gemini models** with **LangChain** and **Chroma** to process, store, and retrieve document data for **question answering**, **summarization**, and **context reasoning** over long documents (50,000+ tokens).

---

## 🎯 Objective  
To develop an intelligent system that can:
- Extract and understand information from **multimodal documents** (text + tables + charts).  
- Perform **semantic chunking and embedding** using Gemini models.  
- Retrieve and generate **context-aware answers** to user queries.  
- Support **long-context processing** and **multi-part questions** efficiently.

---

## ⚙️ Tech Stack  
| Component | Tool / Model |
|------------|---------------|
| **Document Parsing** | `unstructured` |
| **Chunking** | `chunk_by_title` |
| **Embeddings** | `models/gemini-embedding-001` |
| **Vector Store** | `Chroma` |
| **LLM (for Q&A)** | `gemini-2.5-flash` |
| **Framework** | `LangChain` |
| **Language** | Python 3.12+ |

---

## 🧠 Workflow  

1. **Document Extraction**  
   - The system uses `unstructured.partition.pdf` to extract text, tables, and image captions.  

2. **Chunking**  
   - The extracted content is divided into meaningful sections using `chunk_by_title`.  

3. **Embedding Generation**  
   - Each chunk is embedded using **Gemini Embedding Model** (`models/gemini-embedding-001`).  

4. **Storage in Chroma**  
   - All embeddings are stored in **Chroma**, a persistent vector database for efficient semantic retrieval.  

5. **Question Answering**  
   - Users can ask detailed questions about the document.  
   - The system retrieves relevant chunks and generates responses using **Gemini-2.5-Flash**.  

---

## 💡 Example Use Case  

### Use Case: Academic Paper Analyzer  
- Upload a research paper (with figures, charts, or tables).  
- System extracts and embeds all content.  
- Ask:  
  > “Explain Figure 1: The Transformer model architecture.”  
- Output:  
  > Describes the encoder-decoder architecture with self-attention and feed-forward layers, referencing visual elements mentioned in the text.

---

## 🧰 Real-World Applications  
- 📚 Academic research summarization  
- 🏢 Business or financial report analysis  
- ⚖️ Legal and policy document understanding  
- 🧠 Educational assistance for complex PDFs  
- 📊 Chart and table interpretation from documents  


🚀 How to Run
1️⃣ Install Dependencies
pip install requirements.txt

2️⃣ Set Environment Variable (.env)
GOOGLE_API_KEY="your_api_key"

