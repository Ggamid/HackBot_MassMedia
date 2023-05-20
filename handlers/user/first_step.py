from states import GetInfo
from aiogram import types
from keyboards import choose_kind_of_content
from loader import dp


@dp.message_handler(commands="start")
async def choose_content(message: types.Message):
    await message.answer("Здравствуй, выбери какой контент ты хочешь продать. 👇🏻", reply_markup=choose_kind_of_content)
    await GetInfo.getContent.set()

