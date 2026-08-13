#Concurrent (fast — running simultaneously):

import asyncio
import time


async def call_llm(prompt: str, delay: float) -> str:
    print(f"  → Calling LLM: '{prompt}'")
    await asyncio.sleep(delay)
    print(f"  ← LLM responded: '{prompt}'")
    return f"Answer to: {prompt}"


async def concurrent_calls() -> None:
    start = time.perf_counter()

    # asyncio.gather() fires all three simultaneously
    result1, result2, result3 = await asyncio.gather(
        call_llm("What is RAG?", delay=2.0),
        call_llm("What is a vector DB?", delay=1.5),
        call_llm("What are embeddings?", delay=1.0),
    )

    elapsed = time.perf_counter() - start
    print(f"\nConcurrent time: {elapsed:.2f}s")
    # ~2.0 seconds — limited by the LONGEST call, not the sum


asyncio.run(concurrent_calls())