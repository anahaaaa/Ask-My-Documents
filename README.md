<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/VectorDB-ChromaDB-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge&logo=huggingface" />
  <img src="https://img.shields.io/badge/AI-Retrieval--Augmented--Generation-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

<h1 align="center">📚 Ask-My-Documents</h1>

<p align="center">
  A production-grade <strong>Multimodal RAG (Retrieval-Augmented Generation)</strong> system for intelligent document understanding, semantic retrieval, and grounded question answering.
</p>

---

## Overview

**Ask-My-Documents** is an advanced multimodal RAG pipeline designed to process complex documents such as research papers, technical PDFs, and enterprise documents. Unlike basic PDF chatbot implementations, this project focuses on retrieval quality, multimodal understanding, and production-style document ingestion pipelines.

The system combines:

- **Semantic chunking** — title-aware, context-preserving document segmentation
- **OCR-aware extraction** — robust handling of scanned and image-heavy documents
- **Table-aware parsing** — structured preservation of tabular data
- **Image-aware understanding** — vision-language model integration for multimodal content
- **AI-powered semantic enrichment** — LLM-augmented chunk metadata
- **Vector retrieval pipelines** — high-performance semantic search via ChromaDB

---

## Features

| Feature | Description |
|---|---|
| 📄 PDF Ingestion | Parse and extract content from complex PDFs |
| 🧠 Semantic Enrichment | AI-enhanced chunk-level understanding |
| 🖼️ Multimodal Understanding | Vision-Language Model integration (Qwen2-VL) |
| 📊 Table Extraction | Structure-preserving table parsing |
| 🔎 Vector Retrieval | Semantic search with ChromaDB |
| 🧩 Title-Aware Chunking | Context-coherent document segmentation |
| 📚 Grounded Generation | Source-cited answer generation |
| 🏷️ Metadata-Aware Retrieval | Rich metadata for precision filtering |
| 🚀 Production Architecture | Modular, extensible ingestion pipeline |

---

## Tech Stack

| Component | Technology |
|---|---|
| Document Parsing | [Unstructured](https://github.com/Unstructured-IO/unstructured) |
| Embeddings | `BAAI/bge-small-en-v1.5` |
| Vector Database | ChromaDB |
| Multimodal Model | Qwen2-VL |
| Framework | LangChain |
| OCR | Tesseract OCR |
| PDF Processing | Poppler |
| Backend | Python 3.10+ |

---

## System Architecture

```text
Document Upload
      │
      ▼
Document Parsing (Unstructured)
      │
      ▼
Semantic Element Extraction
      │
      ▼
Title-Aware Chunking
      │
      ▼
Multimodal Content Extraction
      │
      ▼
AI Semantic Enrichment
      │
      ▼
Embeddings Generation
      │
      ▼
ChromaDB Vector Storage
      │
      ▼
Hybrid Retrieval + Re-ranking
      │
      ▼
Grounded Answer Generation
```

---

## Project Structure

```
ask-my-documents/
│
├── data/
├── notebooks/
├── src/
│   ├── ingestion/
│   ├── chunking/
│   ├── embeddings/
│   ├── retrieval/
│   ├── llm/
│   ├── evaluation/
│   └── utils/
│
├── vector_db/
├── app/
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ask-my-documents.git
cd ask-my-documents
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install System Dependencies

**Linux:**
```bash
sudo apt-get install poppler-utils tesseract-ocr
```

**Windows:**

Download and install:
- [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases)
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)

Then add both to your system `PATH`.

---

## Current Capabilities

- [x] Semantic document chunking
- [x] Multimodal preprocessing pipeline
- [x] OCR-aware extraction
- [x] Table-aware document understanding
- [x] Image-aware retrieval enrichment
- [x] Vision-language model integration
- [x] Retrieval-ready semantic indexing

---

## Roadmap

- [ ] Hybrid Retrieval (BM25 + Dense Retrieval)
- [ ] Cross-Encoder Re-ranking
- [ ] RAG Evaluation Pipeline (Ragas)
- [ ] Citation-aware responses
- [ ] Streamlit / FastAPI deployment
- [ ] Image embedding retrieval
- [ ] Parent-child retrieval
- [ ] Cross-modal search

---

## Example Use Cases

- 📖 **Research Paper Assistant** — Query academic papers with grounded citations
- 🛠️ **Technical Documentation QA** — Instant answers from complex technical manuals
- 🏢 **Enterprise Document Search** — Retrieve insights from internal knowledge bases
- 📊 **Table-Aware QA** — Ask questions directly about tabular data
- 🌐 **Multimodal Knowledge Retrieval** — Combine text and image understanding

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

Developed as part of an advanced RAG engineering and multimodal retrieval learning journey.