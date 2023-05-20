from aiogram import types
from loader import dp, bot
from keyboards import buy_button_Markup



@dp.message_handler(chat_type=types.ChatType.GROUP)
async def send_lot_func(photo, text):
    # if message['chat']['type'] == "group":
    await bot.send_photo(-742456279, photo=photo, caption=text, reply_markup=buy_button_Markup)
