# handlers/expenses.py
from aiogram import types, Dispatcher
from services.excel_service import add_expense

async def expense_handler(message: types.Message):
    data = message.text.split()
    if len(data) < 4:
        await message.answer("Используйте формат: 'расход <сумма> <категория> <описание>'")
        return
    try:
        amount = float(data[1])
        category = data[2]
        description = " ".join(data[3:])
        add_expense(amount, category, description)
        await message.answer(f"Расход добавлен: {amount} на {category} - {description}")
    except ValueError:
        await message.answer("Неверный формат суммы.")

def register_expense_handlers(dp: Dispatcher):
    dp.message.register(expense_handler)
