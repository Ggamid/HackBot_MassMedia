from aiogram import types
from states import GetInfo
from loader import dp


@dp.message_handler(text="Отправить Контент")
async def getContent(message: types.Message):
    await message.answer(f"Кидай Контент!")
    await GetInfo.getContent.set()


@dp.message_handler(content_types=['photo', 'video', 'text'], state=GetInfo.getContent)
async def getContent_step2(message: types.Message):
    match message.content_type:
        case 'photo':
            pass
        case 'text':
            pass
        case 'video':
            pass


# @dp.message_handler(content_types=["photo"])
# async def send_photo_id(message: types.Message):
#     await message.answer(f"{message.photo[-1].file_id}")
#
#     await bot.send_photo(message.chat.id, f"{message.photo[-1].file_id}")
#
#
# @dp.message_handler(content_types=["video"])
# async def send_photo_id(message: types.Message):
#     await bot.send_message(message.from_user.id, f"{message.video.file_id}")
#     await bot.send_video(message.from_user.id, f"{message.video.file_id}")
