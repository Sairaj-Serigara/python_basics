
import asyncio
import time

async def func1():
    await asyncio.sleep(1)
    print("function 1 done")

async def func2():
    await asyncio.sleep(3)
    print("function 2 done")

async def func3():
    await asyncio.sleep(5)
    print("function 3 done")

async def main():
    task1 = asyncio.create_task(func1())
    task2 = asyncio.create_task(func2())
    task3 = asyncio.create_task(func3())

    await task1
    await task2
    await task3

asyncio.run(main())
