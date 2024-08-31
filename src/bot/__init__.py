from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import async_sessionmaker

from .handlers import root_router
from .middlewares import DbSessionMiddleware


async def start(token: str, *, session_maker: async_sessionmaker) -> None:
    bot = Bot(token=token)

    dp = Dispatcher()
    dp.include_router(handlers.root_router)
    dp.update.middleware(DbSessionMiddleware(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
