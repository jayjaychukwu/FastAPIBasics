import asyncio


# This is an example of a coroutine <async and await keywords>
async def main():
    print("Hello ...")
    await asyncio.sleep(1)
    print("... World!")


asyncio.run(main())
