from utils.config import SYSTEM_PROMPT

def build_prompt(query: str, context_chunks: list[str]):
    context = "\n".join(context_chunks)
    return f"""
{SYSTEM_PROMPT}

Notes:
{context}

Query:
{query}
"""
