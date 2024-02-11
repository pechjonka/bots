import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


bot = Bot(token="6802665061:AAGgO4fmA-VJb0RTbJmja9MaCcJ29N1awrM")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт!')


@dp.message()
async def start_cmd(message: types.Message):
    await message.answer(message.text)
    await message.reply(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
