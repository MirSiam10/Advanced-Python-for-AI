import asyncio


async def background_logging() -> None:
    for i in range(6):
        print(f"Background log: {i + 1}")
        await asyncio.sleep(0.5)


async def short_task(task_number: int) -> None:
    print(f"Short task {task_number} started")
    await asyncio.sleep(0.3)
    print(f"Short task {task_number} completed")


async def main() -> None:
    # Start logging in the background
    logging_task = asyncio.create_task(background_logging())

    # Run 3 short tasks
    await asyncio.gather(
        short_task(1),
        short_task(2),
        short_task(3),
    )

    print("All short tasks completed")

    # Wait for background logging to finish
    await logging_task

    print("Background logging completed")


asyncio.run(main())