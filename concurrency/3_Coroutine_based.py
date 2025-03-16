# Coroutine based concurrency ( asyncio )
# uses async/await syntax
# best for I/O bound tasks ( network request, database queries)
# uses single threaded event loop ( does not create new threads/processes)

import asyncio

async def worker(n):
    print(f"Worker {n} started")
    await asyncio.sleep(2) # simulate work ( non blocking )
    print(f"Worker {n} finished")
    
async def main():
    tasks = [worker(i) for i in range(3)]
    await asyncio.gather(*tasks) # run all coroutines concurrently
    
asyncio.run(main())

#How it works
# the event loop schedules coroutines to run asynchrously
# await asynchio.sleep(2) does not block execution
# multiple coroutines run in one thread

