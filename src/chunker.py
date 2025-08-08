# src/chunker.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("sentence-transformers/distiluse-base-multilingual-cased-v1")

def chunk_text(text, chunk_size=200):
    sentences = text.split("।")
    chunks = []
    chunk = ""
    for sentence in sentences:
        if len(chunk) + len(sentence) < chunk_size:
            chunk += sentence + "।"
        else:
            chunks.append(chunk.strip())
            chunk = sentence + "।"
    if chunk:
        chunks.append(chunk.strip())
    return chunks

def vectorize_chunks(chunks):
    vectors = model.encode(chunks)
    return np.array(vectors), chunks

def create_faiss_index(vectors):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    return index
