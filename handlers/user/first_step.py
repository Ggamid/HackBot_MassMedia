from states import GetInfo
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import choose_kind_of_content, send_content
from loader import dp


@dp.message_handler(commands="start")
async def choose_content(message: types.Message, state: FSMContext):
    await message.answer("Здравствуй, выбери какой контент ты хочешь продать. 👇🏻", reply_markup=send_content)
    await state.finish()

