# src/retriever.py
def retrieve(query, index, chunks, top_k=3):
    q_vec = model.encode([query])
    D, I = index.search(q_vec, top_k)
    return [chunks[i] for i in I[0]]
