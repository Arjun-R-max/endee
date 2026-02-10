from sentence_transformers import SentenceTransformer


class Embedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents):
        return self.model.encode(documents, convert_to_numpy=True)

    def embed_query(self, query: str):
        return self.model.encode([query], convert_to_numpy=True)[0]
