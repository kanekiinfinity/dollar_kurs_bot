import logging


from aiogram import Bot, Dispatcher, executor, types

import valyuta

API_TOKEN = "6742262781:AAFAuNQrYheA00RKv_4ZVVX1ceNxIGL5SL4"

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
db = Dispatcher(bot)

@db.message_handler(commands=['start','help'])
async def bot_start(message: types.Message):
    await message.reply("Assalomu aleykum\nBotimizga xush kelibsiz")
    await message.answer(f"Hozir {valyuta.sana} sana bilan 1 dollat kursi {valyuta.kurs} so'mga teng")



if __name__ == '__main__':
    executor.start_polling(db, skip_updates=True)