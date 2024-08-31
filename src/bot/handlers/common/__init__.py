""" These are common handlers for all types of chats but not including channels """
from aiogram import Router

from . import ping


router = Router()
router.include_routers(
    ping.router,
)
