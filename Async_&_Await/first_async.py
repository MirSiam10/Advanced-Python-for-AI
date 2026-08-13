import asyncio


async def greet(name: str) -> str:
    return f"Hello, {name}!"


# asyncio.run() starts the event loop and runs the coroutine

result = asyncio.run(greet("Alice"))
print(result)   # "Hello, Alice!"