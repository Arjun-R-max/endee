import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class EndeeVectorStore:
    """
    Lightweight Endee-style vector store abstraction
    (acts as the vector database layer for semantic search)
    """

    def __init__(self):
        self.vectors = []
        self.metadata = []

    def add(self, vector, metadata):
        self.vectors.append(vector)
        self.metadata.append(metadata)

    def search(self, query_vector, top_k=3):
        if not self.vectors:
            return []

        vectors_np = np.array(self.vectors)
        similarities = cosine_similarity([query_vector], vectors_np)[0]

        top_indices = similarities.argsort()[::-1][:top_k]

        results = []
        for idx in top_indices:
            results.append({
                "score": float(similarities[idx]),
                "text": self.metadata[idx]["text"]
            })

        return results
