from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from gamedata.gamedata import GameData


class IsInClassList(BoundFilter):
    async def check(self, m: types.Message):
        return m.text in await GameData.get_all_char_classes()