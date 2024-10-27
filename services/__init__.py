# services/__init__.py

from .excel_service import add_expense, add_income, generate_report
from .sheets_service import sync_with_google_sheets  # Допустим, у нас есть функция синхронизации с Google Sheets

__all__ = ["add_expense", "add_income", "generate_report", "sync_with_google_sheets"]
