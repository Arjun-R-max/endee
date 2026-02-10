from scripts.ingest_data import ingest

# Ingest once at module load (efficient & clean)
_embedder, _vector_store = ingest()


def main(query, top_k=3):
    query_vector = _embedder.embed_query(query)
    results = _vector_store.search(query_vector, top_k=top_k)

    print("\n📄 Top Relevant Documents:")
    for idx, res in enumerate(results, start=1):
        print(f"{idx}. ({res['score']:.3f}) {res['text']}")
