import google.generativeai as genai
from utils.config import EMBEDDING_MODEL

def get_gemini_embedding(text: str) -> list[float]:
    res = genai.embed_content(
        model=EMBEDDING_MODEL, content=text, task_type="RETRIEVAL_QUERY"
    )
    return res["embedding"]
