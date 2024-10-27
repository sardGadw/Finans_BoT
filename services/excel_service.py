# services/excel_service.py
from database import add_transaction, get_transactions

def add_expense(amount, category, description):
    add_transaction("расход", amount, category, description)

def add_income(amount, category, description):
    add_transaction("доход", amount, category, description)

def generate_report():
    transactions = get_transactions()
    report = "Отчет о транзакциях:\n"
    for transaction in transactions:
        report += f"{transaction[1]} | {transaction[2]} | {transaction[3]} | {transaction[4]} | {transaction[5]}\n"
    return report
