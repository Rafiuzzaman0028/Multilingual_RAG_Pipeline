# src/preprocess.py

from PyPDF2 import PdfReader
import re

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[\u200c\u200d]', '', text)  # Remove ZWNJ, ZWJ
    return text.strip()
