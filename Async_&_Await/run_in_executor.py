import asyncio
import time


async def fast_task(task_id: int) -> None:
    print(f"Fast task {task_id} started")

    await asyncio.sleep(0.2)

    print(f"Fast task {task_id} completed")


def blocking_operation() -> None:
    print("Blocking operation started")

    time.sleep(2)

    print("Blocking operation completed")


async def fixed_blocking_task() -> None:
    loop = asyncio.get_running_loop()

    await loop.run_in_executor(
        None,
        blocking_operation,
    )


async def main() -> None:
    start = time.perf_counter()

    await asyncio.gather(
        fast_task(1),
        fast_task(2),
        fast_task(3),
        fixed_blocking_task(),
    )

    elapsed = time.perf_counter() - start

    print(f"\nTotal time: {elapsed:.2f} seconds")


asyncio.run(main())