import asyncio


async def producer(queue: asyncio.Queue):
    for number in range(1, 6):
        await asyncio.sleep(0.2)

        await queue.put(number)
        print(f"Produced: {number}")

    # Signal that production is finished
    await queue.put(None)


async def consumer(queue: asyncio.Queue):
    while True:
        number = await queue.get()

        if number is None:
            break

        result = number ** 2

        print(f"Consumed: {number} → {result}")

        queue.task_done()


async def main():
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    await producer_task
    await consumer_task


asyncio.run(main())