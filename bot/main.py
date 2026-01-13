from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
import asyncio
import os

logging.basicConfig(level=logging.INFO)
API_TOKEN = os.environ["API_TOKEN"]
#API_TOKEN = "8033093772:AAEFi6kOkvN0lCFUuqy05Ig1ByFOksQz-fg"  # вставь сюда токен от BotFather

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Привет!\n\n"
        "Я сделаю для тебя профессиональное фото для резюме и LinkedIn за 1 минуту.\n"
        "Загрузи фото, и начнём 👇"
    )

# Получение фото
@dp.message(lambda message: message.photo is not None)
async def photo_handler(message: types.Message):
    photo = message.photo[-1]  # берём наибольшее качество
    file_info = await bot.get_file(photo.file_id)
    file_path = file_info.file_path
    await message.answer(f"Фото получено! 🖼\nФайл: {file_path}\nСкоро начнём обработку (пока это заглушка).")

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))