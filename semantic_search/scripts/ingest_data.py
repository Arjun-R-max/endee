from core.embedder import Embedder
from core.vector_store import EndeeVectorStore

DATA_PATH = "data/documents.txt"


def load_documents(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def ingest():
    documents = load_documents(DATA_PATH)

    embedder = Embedder()
    vector_store = EndeeVectorStore()

    embeddings = embedder.embed_documents(documents)
    for doc, emb in zip(documents, embeddings):
        vector_store.add(emb, {"text": doc})

    return embedder, vector_store
