from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import string


def generate_random_word():
    characters = string.ascii_letters + string.digits
    word = ''.join(random.choices(characters, k=11))
    return word


def generate_InlineKeyboardMarkup():
    buy_button_Markup = InlineKeyboardMarkup(row_width=1)
    random_word = generate_random_word()
    buy_button = InlineKeyboardButton(f"Купить 💸", callback_data=f"{random_word}")
    buy_button_Markup.add(buy_button)
    return [buy_button_Markup, random_word]
