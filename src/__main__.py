import asyncio
import logging

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)

from src import bot
from src.settings import settings

async def main():
    engine = create_async_engine(url=settings.DATABASE_URL, echo=True)
    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    await bot.start(
        settings.BOT_TOKEN.get_secret_value(),
        session_maker=session_maker
    )


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
