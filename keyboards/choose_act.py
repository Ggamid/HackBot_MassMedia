from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

choose_kind_of_content = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Спорт 🏃🏻'),
            KeyboardButton('Региональные 🏘️'),
            KeyboardButton('Экономика 💰')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

send_content = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Отправить Контент'),

        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
