import asyncio
import aiohttp
import time


async def send_request(session, i):
    async with session.get(f"http://localhost:8000/user_{i}") as response:
        return await response.text()


async def load_test(total_request):
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, i) for i in range(total_request)]
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        end_time = time.time()
        print(f"Finished {len(results)} results in {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(load_test(1000000))
