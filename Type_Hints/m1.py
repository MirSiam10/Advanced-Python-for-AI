#Medium Exercise: Write a function that takes a string as input and returns a list of floats representing the word's embedding. Use type hints to specify the input and output types.

def find_embedding(word: str) -> list[float] | None:
    """
    Return a fake embedding for a word if it exists.

    Args:
        word: The word to search for.

    Returns:
        A list of three floats representing the embedding,
        or None if the word is not found.
    """
    embeddings: dict[str, list[float]] = {
        "python": [0.12, 0.85, 0.43],
        "ai": [0.91, 0.22, 0.67],
        "chatbot": [0.33, 0.78, 0.55],
    }

    return embeddings.get(word.lower())
