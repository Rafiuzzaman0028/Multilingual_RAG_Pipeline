# src/api.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from preprocess import extract_text_from_pdf, clean_text
from chunker import chunk_text, vectorize_chunks, create_faiss_index
from retriever import retrieve
from generator import generate_answer
from memory import ChatMemory
import uvicorn

app = FastAPI()
memory = ChatMemory()

# Load data and index at startup
text = clean_text(extract_text_from_pdf("data/HSC26_Bangla_1st.pdf"))
chunks = chunk_text(text)
vectors, chunks = vectorize_chunks(chunks)
index = create_faiss_index(vectors)

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(query: Query):
    question = query.question
    context_chunks = retrieve(question, index, chunks)
    context = " ".join(context_chunks)
    answer = generate_answer(question, context)
    memory.add(question, answer)
    return {"answer": answer}
