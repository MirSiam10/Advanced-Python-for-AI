'''M2. Write an async function safe_fetch(url: str) -> str | None that calls a simulated async_get(url: str) -> str function (which randomly raises a ConnectionError 50% of the time). safe_fetch should catch the error, print a warning, and return None. Run 5 safe_fetch calls concurrently with gather().'''


import asyncio
import random

async def async_get(url:str)-> str:

    await asyncio.sleep(1)

    if random.random() < 0.5:
        raise ConnectionError(f"Failed to connect to {url}")
    return f"Data from {url}"

async def safe_fech(url:str)-> str|None:

    try:
        result = await async_get(url)
        return result

    except ConnectionError as error:
        print(f"Warning{error}")
        return None

    
async def main()->None:

    urls = [
        "https://api.example.com/users",
        "https://api.example.com/posts",
        "https://api.example.com/products",
        "https://api.example.com/orders",
        "https://api.example.com/comments"
    ]

    results = await asyncio.gather(
        *(safe_fech(url) for url in urls)

    )

    print("\nResults")

    for url, result in zip(urls, results):
        print(f"{url}->{result}")


asyncio.run(main())

