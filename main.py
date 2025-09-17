# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters import Command
# from config import BOT_TOKEN
# import random

# API_TOKEN = BOT_TOKEN

# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
# quizes = ["Сколько примерно озер в Кении?", "Какое название 2 по высоте горе?", "Является ли данный телеграм бот полезным?"]
# answers = ["64", "Дыхтау", "Да"]

# @dp.message(Command("start"))
# async def start_message(message: types.Message):
#     await message.answer("?")

# # @dp.message(lambda message: message.text.lower() == "help")
# # async def help_message(message: types.Message):
# #     await message.answer("Я ничего не умею")

# @dp.message(lambda message: message.text.lower() == "?")
# async def answer_how(message: types.Message):
#     await message.answer("!")

# # @dp.message(Command("quiz"))
# # async def quiz_message(message: types.Message):
# #     rand = random.randint(0, len(quizes) - 1)
# #     await message.answer(rand)

# if __name__ == '__main__':
#     dp.run_polling(bot)