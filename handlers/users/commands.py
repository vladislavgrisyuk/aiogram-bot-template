from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Text

from filters.filter_classes import IsInClassList
from gamedata.gamedata import GameData
from keyboards.default import char_class_menu
from keyboards.default.char_class_menu import GameButtons
from keyboards.inline.callback_data import choice_callback
from keyboards.inline.inline_create_menu import choice
from loader import dp
from loader import bot
from states import CreateChar

import emoji


@dp.message_handler(lambda message: message.text.lower() == 'создать персонажа')
async def bot_echo(message: types.Message):
    if await GameData.user_already_exists(message.from_user.id) == 0:
        await CreateChar.s1.set()
        await message.answer("Ну нихуя ты авантюрист, выбери своего бойца:",reply_markup=await GameButtons.choose_class_btns(), reply=True)
    else:
        await message.reply("Ты ебнутый? У тебя уже есть твой персонаж...")


@dp.message_handler(lambda message: message.text.lower() == 'нахуй кнопки')
async def bot_echo(message: types.Message, state: FSMContext):
    data = await state.get_data()
    char_class = data.get("s2")
    await message.answer(emoji.emojize('lol :poop:', use_aliases=True), reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(IsInClassList(), state=CreateChar.s1)
async def send_echo(m: types.Message, state: FSMContext):
    await state.finish()
    await GameData.create_user_character(m.from_user.id, m.text)
    await m.answer(emoji.emojize(f'Заебись {m.from_user.username}, ты теперь {m.text}:poop:', use_aliases=True), reply_markup=ReplyKeyboardRemove())


@dp.message_handler(lambda m : m.text.lower() in ['колдун'], state=CreateChar.s1)
async def send_echo(m: types.Message, state: FSMContext):
    await state.finish()
    await m.answer(emoji.emojize(f'Заебись {m.from_user.username}, тыЫФЫВЫФВ теперь {m.text}:poop:', use_aliases=True))


@dp.message_handler(lambda m : m.text.lower() in ['log'])
async def send_echo(m: types.Message, state: FSMContext):
    await state.finish()




