from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buy_button_Markup = InlineKeyboardMarkup(row_width=1)

buy_button = InlineKeyboardButton(f"Купить 💸", callback_data="right")

