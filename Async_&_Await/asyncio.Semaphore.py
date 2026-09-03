"""Goal: Only 2 API calls should run at the same time."""

import asyncio
import time


semaphore = asyncio.Semaphore(2)


async def api_call(call_id: int):
    async with semaphore:
        print(f"API call {call_id} started")

        await asyncio.sleep(1)

        print(f"API call {call_id} finished")


async def main():
    start = time.perf_counter()

    tasks = [api_call(i) for i in range(1, 7)]

    await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start

    print(f"\nTotal time: {elapsed:.2f} seconds")


asyncio.run(main())