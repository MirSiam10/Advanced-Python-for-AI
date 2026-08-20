import asyncio
import time

async def get_user(user_id: int) -> str:
    print(f"Fetching user...")
    await asyncio.sleep(1)
    return f"user {user_id}"
async def get_user_posts(user_id: int)-> list[str]:
    print(f"Fetching posts....")
    await asyncio.sleep(3)
    return [
        f"Post 1 by user {user_id}",
        f"Post 2 by user {user_id}"
    ]

async def main ()-> None:
    start = time.perf_counter()

    user = await get_user(121)
    posts = await get_user_posts(121)

    end = time.perf_counter()

    print(user)
    print(posts) 
    print(f"Total time: {end - start:.2f} seconds")

asyncio.run(main())


