import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        a = 1 #Make this normal lol