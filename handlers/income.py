# handlers/income.py
from aiogram import types, Dispatcher
from services.excel_service import add_income

async def income_handler(message: types.Message):
    data = message.text.split()
    if len(data) < 4:
        await message.answer("Используйте формат: 'доход <сумма> <категория> <описание>'")
        return
    try:
        amount = float(data[1])
        category = data[2]
        description = " ".join(data[3:])
        add_income(amount, category, description)
        await message.answer(f"Доход добавлен: {amount} на {category} - {description}")
    except ValueError:
        await message.answer("Неверный формат суммы.")

def register_income_handlers(dp: Dispatcher):
    dp.message.register(income_handler)
