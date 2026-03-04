import asyncio

queue = asyncio.Queue()

async def add_job(job):
    await queue.put(job)

async def worker():
    while True:
        job = await queue.get()
        try:
            await job()
        except Exception as e:
            print("Job error:", e)
        queue.task_done()