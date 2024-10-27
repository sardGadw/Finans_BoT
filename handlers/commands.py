# handlers/commands.py
from aiogram import types, Dispatcher
from aiogram.filters import Command

async def start_handler(message: types.Message):
    await message.answer("Привет! Этот бот поможет вам вести учет доходов и расходов. Отправьте команду /help для списка команд.")

def register_command_handlers(dp: Dispatcher):
    dp.message.register(start_handler, Command("start"))
