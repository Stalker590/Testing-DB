import asyncio
import sys
import logging
from queries.orm import create_tables, insert_data
import asyncio

async def main():
    await create_tables()
    await insert_data("Bajaj Boxer 150X", 1400)

if __name__ == "__main__":
    import sys
    if sys.platform.startswith("win"):
        import asyncio
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())