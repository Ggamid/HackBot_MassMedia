from loader import dp
from aiogram import types
from wrkDB import get_lot_data_with_lot_id
from loader import bot


@dp.callback_query_handler()
async def go_to_ls(callback: types.CallbackQuery):
    await callback.message.edit_caption(f"Заморожено 🧊")

    data = get_lot_data_with_lot_id(callback.data)
    text = data[1]
    photo_id = data[0]
    price = data[2]
    username = data[3]

    await bot.send_photo(callback['from']['id'], photo_id, f"{text} \n\n Цена 💸:{price} \n\n@{username}", parse_mode="HTML")
