# Bengali-English RAG Pipeline 📚

A multilingual Retrieval-Augmented Generation (RAG) system for processing Bengali educational content, built with FAISS, Sentence-Transformers, and OpenAI/T5 models.

![RAG Pipeline Diagram](https://miro.medium.com/v2/resize:fit:1400/1*5ZLci3SuR0zM_QlZOADv8Q.png)

## Features

- Extracts and processes Bengali text from PDF documents
- Multilingual embeddings using `distiluse-base-multilingual-cased-v2`
- FAISS vector store for efficient similarity search
- Answer generation with:
  - OpenAI models (English)
  - BanglaT5 (Bengali)
- Evaluation metrics for answer quality

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rafiuzzaman0028/Multilingual_RAG_Pipeline.git
   cd Multilingual_RAG_Pipeline


Install dependencies:

bash
pip install -r requirements.txt

Usage
1. Process PDF Documents
python
from pdf_processing import extract_text_from_pdf
raw_text = extract_text_from_pdf("data/HSC26-Bangla1st-Paper.pdf")

2. Run the RAG Pipeline
python
from pipeline import BengaliRAGPipeline

pipeline = BengaliRAGPipeline()
pipeline.load_documents("data/HSC26-Bangla1st-Paper.pdf")
answer = pipeline.query("অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?")
print(answer)

Sample Queries
"অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?"

"কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?"

"বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?"


File Structure
text
.
├── notebooks/               # Jupyter notebooks for development
│   └── Bengali_English_RAG_Pipeline.ipynb
├── src/                     # Python source files
│   ├── __init__.py
│   ├── pdf_processing.py    # PDF text extraction
│   ├── embedding.py         # Text embedding logic
│   └── rag.py              # RAG pipeline implementation
├── data/                    # Sample documents
├── requirements.txt         # Python dependencies
└── README.md
Dependencies
Python 3.8+

PyMuPDF (for PDF processing)

Sentence-Transformers

FAISS

Transformers (HuggingFace)

BanglaT5 or other Bengali language models
