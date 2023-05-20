from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config


storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN)

dp = Dispatcher(bot, storage=storage)