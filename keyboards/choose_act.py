from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

get_permission = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('ДА! 🤩'),
            KeyboardButton('НЕТ! 🫤')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)

send_content = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Отправить Контент 📸'),

        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
