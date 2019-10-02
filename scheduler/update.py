from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .apps import RepoPuller

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(RepoPuller, 'interval', minutes=15)
    scheduler.start()