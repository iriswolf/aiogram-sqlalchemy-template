from aiogram import Router
from . import common, chat, private, channel

root_router = Router(name='root router')
root_router.include_routers(
    common.router
)
