from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Text
from keyboards.default import char_class_menu
from keyboards.inline.callback_data import choice_callback
from keyboards.inline.inline_create_menu import choice
from loader import dp
from loader import bot
from states import CreateChar

@dp.message_handler(lambda message: message.text.lower() == 'создать персонажа')
async def bot_echo(message: types.Message):
    await CreateChar.s1.set()
    await message.answer("Выберите персонажа из меню ниже: ", reply_markup=choice)


@dp.callback_query_handler(choice_callback.filter(item_name=(["Воин", "Маг"])))
async def buy_pear(call: types.CallbackQuery, callback_data: dict):
    await call.answer("sd")
    await call.message.answer("dqwdasdasd")


@dp.message_handler(lambda message: message.text.lower() == 'ебнуть')
async def bot_echo(message: types.Message, state: FSMContext):
    data = await state.get_data()
    char_class = data.get("s2")
    await message.answer(f"Боже, мистер {char_class}, как же вы ебнули...")

