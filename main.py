import asyncio
import fetcher as f

async def main():
    raw = await f.Fetcher.General.get_stats()
    for k, v in raw.items():
        print(k, v)

if __name__ == "__main__":
    asyncio.run(main())