from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

choose_kind_of_content = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Фото 📸'),
            KeyboardButton('Виде 📹'),
            KeyboardButton('Текст 💬')
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
