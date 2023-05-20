from aiogram import types
from states import GetInfo
from aiogram.dispatcher import FSMContext
from loader import dp
from handlers.group.send_lot import send_lot_func


@dp.message_handler(text="Отправить Контент")
async def getContent(message: types.Message):
    await message.answer(f"Кидай Контент который станет обложкой твоего лота! (если нет фото и видео введи 'Next')")
    await GetInfo.getContent.set()


@dp.message_handler(content_types=['photo', 'video', 'text'], state=GetInfo.getContent)
async def getContent_step2(message: types.Message, state: FSMContext):
    match message.content_type:
        case 'photo':
            answer = message.photo[-1].file_id
            await state.update_data(getContent=answer)
            await GetInfo.getText.set()
            return

        case 'text':
            await GetInfo.getText.set()
            return


@dp.message_handler(content_types=['text'], state=GetInfo.getText,)
async def getContent_step3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(getText=answer)
    await message.answer("Твой лот будет выглядеть так:")

    data = await state.get_data()
    photo = data.get("getContent")
    text = f"{data.get('getText')}"

    await message.answer_photo(photo, text)
    await state.finish()
    await send_lot_func(photo, text)
    return

