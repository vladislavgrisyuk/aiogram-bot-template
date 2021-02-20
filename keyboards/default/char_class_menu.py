from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db

menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='SUKA')]], selective=True, resize_keyboard=True)

class GameButtons:
    @staticmethod
    async def choose_class_btns():
        classes = await db.get_char_classes()
        gkeyboard = []
        buttons = []
        for key in classes:
            arr = []
            arr.append(KeyboardButton(text=key.get('name')))
            gkeyboard.append(arr)
            print(arr)
        menu = ReplyKeyboardMarkup(keyboard=gkeyboard, selective=True, resize_keyboard=True)
        return menu

