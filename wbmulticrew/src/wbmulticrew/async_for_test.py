import asyncio
import random
import time


async def async_task(i):
    await asyncio.sleep(random.random() * 5)  # simulate IO-bound task with random delay
    return i


async def main():
    tasks = [async_task(i) for i in range(5)]
    for future in asyncio.as_completed(tasks):
        result = await future
        print(result)


# Run the async function
start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds.")
