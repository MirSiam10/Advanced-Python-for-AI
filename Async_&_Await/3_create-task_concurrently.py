import asyncio


async def fetch_user_profile(request_id: int) -> str:
    await asyncio.sleep(0.4)
    return f"Profile for request {request_id}"


async def check_cache(request_id: int) -> str:
    await asyncio.sleep(0.1)
    return f"Cache checked for request {request_id}"


async def log_request(request_id: int) -> str:
    await asyncio.sleep(0.2)
    return f"Request {request_id} logged"


async def handle_request(request_id: int) -> dict:
    profile, cache, log = await asyncio.gather(
        fetch_user_profile(request_id),
        check_cache(request_id),
        log_request(request_id),
    )

    return {
        "request_id": request_id,
        "profile": profile,
        "cache": cache,
        "log": log,
    }


async def main() -> None:
    # Create 3 requests concurrently
    tasks = [
        asyncio.create_task(handle_request(1)),
        asyncio.create_task(handle_request(2)),
        asyncio.create_task(handle_request(3)),
    ]

    results = await asyncio.gather(*tasks)

    for result in results: 
        print(result)


asyncio.run(main())