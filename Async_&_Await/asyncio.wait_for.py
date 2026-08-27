
#Rather than manually cancelling, use the built-in timeout wrapper:

import asyncio


async def slow_llm_call(prompt: str) -> str:
    await asyncio.sleep(5)   # takes 5 seconds
    return f"Response to: {prompt}"


async def main() -> None:
    try:
        # Cancel automatically if it takes more than 2 seconds
        result = await asyncio.wait_for(
            slow_llm_call("What is the meaning of life?"),
            timeout=2.0,
        )
        print(result)
    except asyncio.TimeoutError:
        print("LLM call timed out after 2 seconds")


asyncio.run(main())