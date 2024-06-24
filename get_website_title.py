import os.path

from asyncflows import AsyncFlows


async def main():
    dirname = os.path.dirname(__file__)
    flow = AsyncFlows.from_file(
        os.path.join(dirname, "get_website_title.yaml")
    )

    # Run the flow and return the default output (result of the extract_title action)
    result = await flow.set_vars(
        url="https://en.wikipedia.org/wiki/Python_(programming_language)",
    ).run()
    print(result)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())