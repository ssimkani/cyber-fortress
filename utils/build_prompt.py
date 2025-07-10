def build_prompt(query: str, context_chunks: list[str]):
    context = "\n".join(context_chunks)
    return f"""Use notes to answer the query:

Notes:
{context}

Query:
{query}
"""
