from aiogram.dispatcher.filters.state import State, StatesGroup


class GetInfo(StatesGroup):
    getContent = State()
    getText = State()
    getPrice = State()
    getPermission = State()