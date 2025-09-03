import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import BOT_TOKEN

API_TOKEN = BOT_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_message(message: types.Message):
    await message.answer("hello")

@dp.message(lambda message: message.text.lower() == "help")
async def help_message(message: types.Message):
    await message.answer("Я ничего не умею")

@dp.message(lambda message: message.text.lower() == "?")
async def answer_how(message: types.Message):
    await message.answer("Я тг бот")

if __name__ == '__main__':
    dp.run_polling(bot)