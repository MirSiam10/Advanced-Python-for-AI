import asyncio
import time

from pydantic import BaseModel, Field


class RAGConfig(BaseModel):
    top_k: int = Field(default=3, ge=1)
    similarity_threshold: float = Field(default=0.7, ge=0.0, le=1.0)


async def embed_query(query: str) -> list[float]:
    """Simulate converting a query into an embedding."""
    await asyncio.sleep(0.3)

    embedding = [0.12, 0.45, 0.78, 0.91]

    print("✓ Query embedding completed")

    return embedding


async def retrieve_documents(
    embedding: list[float],
    config: RAGConfig
) -> list[str]:
    """Simulate retrieving the most relevant documents."""
    await asyncio.sleep(0.5)

    documents = [
        f"Document {i}: Information relevant to the query"
        for i in range(1, config.top_k + 1)
    ]

    print(f"✓ Document retrieval completed ({len(documents)} documents)")

    return documents


async def generate_response(
    query: str,
    documents: list[str]
) -> str:
    """Simulate generating an answer using retrieved documents."""
    await asyncio.sleep(1.0)

    response = (
        f"Answer to '{query}' based on "
        f"{len(documents)} retrieved documents."
    )

    print("✓ Response generation completed")

    return response


async def run_rag(
    query: str,
    config: RAGConfig
) -> str:
    """Run the complete RAG pipeline."""

    embedding = await embed_query(query)

    documents = await retrieve_documents(
        embedding,
        config
    )

    response = await generate_response(
        query,
        documents
    )

    return response


async def main() -> None:
    config = RAGConfig(
        top_k=3,
        similarity_threshold=0.7
    )

    query = "What is asynchronous programming in Python?"

    print(f"Query: {query}")
    print("-" * 50)

    start = time.perf_counter()

    response = await run_rag(query, config)

    elapsed = time.perf_counter() - start

    print("-" * 50)
    print(f"Final response: {response}")
    print(f"Total pipeline time: {elapsed:.2f} seconds")


asyncio.run(main())