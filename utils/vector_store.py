from pinecone import Pinecone, ServerlessSpec
from utils.embedder import get_gemini_embedding
from utils.config import PINECONE_API_KEY, PINECONE_INDEX_NAME, NUM_CHUNKS

pc = Pinecone(api_key=PINECONE_API_KEY)

if not pc.has_index(PINECONE_INDEX_NAME):
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

index = pc.Index(PINECONE_INDEX_NAME)

def upsert_chunks(uid, chunks: list[str]):
    vectors = []
    for i, chunk in enumerate(chunks):
        embedding = get_gemini_embedding(chunk)
        vectors.append(
            {
                "id": f"{uid}_chunk_{i}",
                "values": embedding,
                "metadata": {"text": chunk, "uid": uid},
            }
        )
    index.upsert(vectors=vectors)


def search_top_k(uid, query: str, k=NUM_CHUNKS) -> list[str]:
    query_vec = get_gemini_embedding(query)
    results = index.query(
        vector=query_vec, top_k=k, include_metadata=True, filter={"uid": {"$eq": uid}}
    )
    return [match["metadata"]["text"] for match in results["matches"]]
