# src/memory.py
class ChatMemory:
    def __init__(self, max_len=5):
        self.history = []
        self.max_len = max_len

    def add(self, user_input, response):
        self.history.append((user_input, response))
        if len(self.history) > self.max_len:
            self.history.pop(0)

    def get_context(self):
        return "\n".join([f"User: {q}\nBot: {a}" for q, a in self.history])
