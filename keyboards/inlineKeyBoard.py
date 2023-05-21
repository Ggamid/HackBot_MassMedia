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


def yes_no():
    yes_no_Markup = InlineKeyboardMarkup(row_width=2)
    yes = InlineKeyboardButton(f"ДА! 🤩", callback_data=f"YES")
    no = InlineKeyboardButton(f"НЕТ 🫤", callback_data=f"NO")
    yes_no_Markup.add(yes, no)
    return yes_no_Markup
