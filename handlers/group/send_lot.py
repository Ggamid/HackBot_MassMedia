from aiogram import types
from loader import dp


@dp.message_handler(chat_type=types.ChatType.GROUP)
async def send_lot_func(message: types.Message):
    await message.answer("123")
