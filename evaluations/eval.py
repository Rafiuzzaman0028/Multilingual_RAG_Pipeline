# evaluations/eval.py
from retriever import retrieve
from generator import generate_answer

def evaluate(query, expected, index, chunks):
    context = " ".join(retrieve(query, index, chunks))
    answer = generate_answer(query, context)
    print(f"Q: {query}\nExpected: {expected}\nPredicted: {answer}")
    print("----")

# Test examples
evaluate("অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?", "শুম্ভুনাথ", index, chunks)
evaluate("কাকে অনুপমের ভাগ্য দেবতা বলে উল্লেখ করা হয়েছে?", "মামাকে", index, chunks)
evaluate("বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?", "১৫ বছর", index, chunks)
