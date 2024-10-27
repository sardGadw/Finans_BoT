# handlers/__init__.py
from .commands import register_command_handlers
from .expenses import register_expense_handlers
from .income import register_income_handlers
from .reports import register_report_handlers

def register_all_handlers(dp):
    register_command_handlers(dp)
    register_expense_handlers(dp)
    register_income_handlers(dp)
    register_report_handlers(dp)
