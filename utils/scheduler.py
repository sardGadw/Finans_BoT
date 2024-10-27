# utils/scheduler.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

def start_scheduler():
    scheduler.start()

def add_job(func, trigger, **kwargs):
    scheduler.add_job(func, trigger, **kwargs)
