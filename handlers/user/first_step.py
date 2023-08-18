from states import GetInfo
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards import get_permission, send_content
from loader import dp


@dp.message_handler(commands="start")
async def choose_content(message: types.Message, state: FSMContext):
    await message.answer("Здравствуй, жми на кнопку ниже 👇🏻 и начнем!", reply_markup=send_content)
    await state.finish()

