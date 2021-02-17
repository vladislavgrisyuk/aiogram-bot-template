from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data import choice_callback

buttons = [
    [
        InlineKeyboardButton(text="Воин", callback_data=choice_callback.new(item_name="Воин"))
    ],
    [
        InlineKeyboardButton(text="Маг", callback_data=choice_callback.new(item_name="Маг"))
    ]
]
choice = InlineKeyboardMarkup(row_width=2, inline_keyboard = [
    [
        InlineKeyboardButton(text="Воин", callback_data=choice_callback.new(item_name="Воин"))
    ],
    [
        InlineKeyboardButton(text="Маг", callback_data="choice:Воин")
    ]
])
