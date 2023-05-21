from aiogram import types
from states import GetInfo
from aiogram.dispatcher import FSMContext
from loader import dp
from handlers.group.send_lot import send_lot_func
from keyboards import get_permission, yes_no
from utils.check_int import check


@dp.message_handler(text="Отправить Контент 📸")
async def getContent(message: types.Message):
    await message.answer(f"Кидай картинку которая станет обложкой твоей новости! 📸💬", parse_mode="HTML")
    await GetInfo.getContent.set()


@dp.message_handler(content_types=['photo'], state=GetInfo.getContent)
async def getContent_step2(message: types.Message, state: FSMContext):
    print()
    await message.answer("Теперь отправь текст 💬. Вначале стоит уделить один абзац краткому и цепляющему описанию 📝")
    answer = message.photo[-1].file_id
    await state.update_data(getContent=answer)
    await GetInfo.getText.set()
    return


@dp.message_handler(state=GetInfo.getContent)
async def getContent_step2_error(message: types.Message):
    await message.answer("Отправьте фото")


@dp.message_handler(content_types=['text'], state=GetInfo.getText, )
async def getContent_step3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(getText=answer)


    await message.answer(
        "А теперь нужно указать цену 💰. \n\n P.s не стоит сильно завышать цену, т.к вашу новость просто никто не купит)")

    data = await state.get_data()
    photo = data.get("getContent")
    text = f"{data.get('getText')}"

    await message.answer_photo(photo, text)
    await GetInfo.getPrice.set()
    # await send_lot_func(photo, text, message.from_user.id)
    return


@dp.message_handler(state=GetInfo.getText)
async def getContent_step3_error(message: types.Message):
    await message.answer("Отправьте текст")


@dp.message_handler(content_types=['text'], state=GetInfo.getPrice, )
async def getContent_step4(message: types.Message, state: FSMContext):
    if not check(message.text):
        await getContent_step4_error(message)
        return

    answer = message.text
    await state.update_data(getPrice=answer)
    await message.answer("Вот что получилось:")

    data = await state.get_data()
    photo = data.get("getContent")
    text = f"{data.get('getText')}"
    price = f"{data.get('getPrice')}"

    await message.answer_photo(photo, f"{text} \n\n Цена: {price} 💸")
    await message.answer("Будем публиковать для репортеров?", reply_markup=yes_no())
    await GetInfo.getPermission.set()


@dp.message_handler(state=GetInfo.getPrice)
async def getContent_step4_error(message):
    await message.answer("Отправьте число")


@dp.callback_query_handler(state=GetInfo.getPermission)
async def getContent_step5(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "YES":
        await callback.answer('Готово! Ваша новость опубликована')
        data = await state.get_data()
        photo = data.get("getContent")
        text = f"{data.get('getText')}"
        price = f"{data.get('getPrice')}"

        await callback.message.answer_photo(photo, f"{text} \n\n Цена: {price} 💸")
        await state.finish()
        print(callback)
        await send_lot_func(photo, text, callback.message.from_user.id, price, callback.message["chat"]['username'])
        return
    else:
        await callback.answer("Окей, мы удалим эти данные")
        await state.finish()
