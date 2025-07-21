from utils.config import SYSTEM_PROMPT


def build_prompt(query: str, context_chunks: list[str]):
    context = "\n\n".join(
        [f"#{i+1}\n{chunk.strip()}" for i, chunk in enumerate(context_chunks)]
    )
    examples = "\n\n".join([f"Q: {ex['question']}\nA: {ex['answer']}" for ex in EXAMPLES])

    return f"""
{SYSTEM_PROMPT}

Notes:
{context}

Query:
{query}
"""
