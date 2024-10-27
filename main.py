# main.py
import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import register_all_handlers
from database import init_db

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    init_db()
    register_all_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

