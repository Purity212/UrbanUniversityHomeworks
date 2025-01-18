from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7624346665:AAF_vHaJTuknJESwfZ9HpDTzovezXojqR44"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler() #декоратор для работы с сообщениями
async def all_message(message):
    print('Сообщение')


@dp.message_handler(text=['z', 'a'])
async def urban_message(message):
    print('text')

@dp.message_handler(commands=['start'])
async def start_message(message):
    print('command')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


