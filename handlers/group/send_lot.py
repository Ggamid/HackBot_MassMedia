from aiogram import types
from loader import dp, bot
from keyboards import generate_InlineKeyboardMarkup
from wrkDB import addLot


@dp.message_handler(chat_type=types.ChatType.GROUP)
async def send_lot_func(photo, text, user_id):
    # if message['chat']['type'] == "group":
    random_word = generate_InlineKeyboardMarkup()
    addLot(user_id, photo, text, random_word[1])

    await bot.send_photo(-742456279, photo=photo, caption=text, reply_markup=random_word[0])

