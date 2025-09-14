import asyncio

async def bar():
    print("bar()")

async def foo():
    print("foo()")

async def main():
    task = asyncio.create_task(foo())
    for _ in range(3):
        await bar()     # bar executes as a sync function here
    await task

if __name__ == "__main__":
    asyncio.run(main())

