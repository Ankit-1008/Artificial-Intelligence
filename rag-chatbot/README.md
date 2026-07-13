# 📚 RAG Chatbot – Chat with PDFs using AI

A Retrieval-Augmented Generation (RAG) based chatbot that allows users to upload PDFs and ask questions about their content using AI.

Built using **LangChain, ChromaDB, Streamlit, and OpenAI / open-source models**.

---

# 🚀 Demo

> Upload a PDF → Ask questions → Get AI answers grounded in your document

Example:
- "Summarize this document"
- "What are the key points in chapter 2?"
- "Explain section 3 in simple terms"

---

# 🧠 Architecture
            ┌──────────────┐
            │   PDF Upload │
            └──────┬───────┘
                   │
                   ▼
        ┌────────────────────┐
        │ Document Loader     │
        │ (LangChain PDF)     │
        └────────┬───────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ Text Chunking      │
        │ (Recursive Split)  │
        └────────┬───────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ Embeddings         │
        │ BGE / OpenAI       │
        └────────┬───────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ Vector DB          │
        │ ChromaDB           │
        └────────┬───────────┘
                 │
    ┌────────────▼────────────┐
    │   User Query            │
    └────────────┬────────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ Similarity Search   │
        │ Top-K Chunks        │
        └────────┬───────────┘
                 │
                 ▼
        ┌────────────────────┐
        │ LLM (GPT / Llama)  │
        │ Answer Generation   │
        └────────┬───────────┘
                 │
                 ▼
           💬 Final Answer


---

# ⚙️ Features

- 📄 Upload and chat with PDF documents
- 🔍 Semantic search using embeddings
- 🧠 RAG (Retrieval-Augmented Generation)
- 💬 AI answers based only on context
- 📚 Source-aware responses
- ⚡ Fast Streamlit UI
- 🔁 Supports OpenAI + local models

---

# 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Frontend | Streamlit |
| Backend | Python |
| Framework | LangChain |
| Vector DB | ChromaDB |
| Embeddings | BAAI/bge-small-en-v1.5 / OpenAI |
| LLM | GPT-4o-mini / Llama 3 |
| Loader | PyPDF |

---

# 📁 Project Structure
rag-chatbot/
│
├── app.py
├── requirements.txt
├── .env
│
├── chroma_db/
│
└── src/
├── document_loader.py
├── text_splitter.py
├── vector_store.py
├── chatbot.py


---

# 🚀 Installation

## 1. Clone repo

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot

python -m venv venv
venv\Scripts\activate #windows

python3 -m venv venv
source venv/bin/activate #mac/linux

