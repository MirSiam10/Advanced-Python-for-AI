
'''M1. Write an async function batch_embed(texts: list[str]) -> list[list[float]] that takes a list of strings and "fetches" an embedding for each one concurrently. Each individual embed call should take 0.5 seconds. Time the difference between sequential and concurrent approaches for 5 texts.'''

import asyncio
import time

async def embed(text: str)-> list[float]:


    await asyncio.sleep(.5)
    return [.1,.2,.3,.4,.5]

async def batch_embed (texts:list[str])-> list[list[float]]:

    results = await asyncio.gather(

        *(embed(text) for text in texts)
    )

    return results

async def sequential_embed(texts: list[str]) -> list[list[float]]:

    results = []

    for text in texts:
        result = await embed(text)
        results.append(result)

    return results

async def main()-> None:

    texts = [
        "Hello world",
        "Python is powerful",
        "I am learning asyncio",
        "AI is interesting",
        "Embeddings are useful"
    ]

    start = time.perf_counter()
    sequential_results = await sequential_embed(texts)
    sequential_time = time.perf_counter() - start

    print(f"Sequential results: {sequential_results}")
    print(f"Sequential time: {sequential_time:.2f} seconds")


    #Concurrent

    start = time.perf_counter()

    concurrent_results = await batch_embed(texts)

    concurrent_time = time.perf_counter() - start

    print(f"Concurrent Result: {concurrent_results}")
    print(f"Concurrent Time: {concurrent_time:.2f} Seconds")


asyncio.run(main())



