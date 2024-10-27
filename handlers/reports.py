# handlers/reports.py
from aiogram import types, Dispatcher
from services.excel_service import generate_report

async def report_handler(message: types.Message):
    report = generate_report()
    await message.answer(report)

def register_report_handlers(dp: Dispatcher):
    dp.message.register(report_handler, commands=['report'])
