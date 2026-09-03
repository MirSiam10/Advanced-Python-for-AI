
"""Create a RateLimiter that:

Allows only 3 operations at once
Tracks the number of operations currently in-flight
Prints when a slot is acquired/released
Tests with 8 concurrent API calls
"""

import asyncio
 
class RateLimiter:
    def __init__(self, limit: int):
        self.semaphore = asyncio.Semaphore(limit)
        self.in_flight = 0

    async def acquire(self):
        await self.semaphore.acquire()

        self.in_flight += 1
        print(f"[ACQUIRED] In-flight: {self.in_flight}")

    def release(self):
        self.in_flight -= 1
        print(f"[RELEASED] In-flight: {self.in_flight}")

        self.semaphore.release()


async def api_call(call_id: int, limiter: RateLimiter):
    await limiter.acquire()

    try:
        print(f"API call {call_id} started")

        await asyncio.sleep(1)

        print(f"API call {call_id} finished")

    finally:
        limiter.release()


async def main():
    limiter = RateLimiter(limit=3)

    tasks = [
        asyncio.create_task(api_call(i, limiter))
        for i in range(1, 9)
    ]

    await asyncio.gather(*tasks)


asyncio.run(main())