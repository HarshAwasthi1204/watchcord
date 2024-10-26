from celery import Celery
import os
from dotenv import load_dotenv

BROKER_URL = os.getenv("BROKER_URL")
BACKEND_URL = os.getenv("BACKEND_URL")
if not BROKER_URL or not BACKEND_URL:
    load_dotenv()
    BROKER_URL = os.getenv("BROKER_URL")
    BACKEND_URL = os.getenv("BACKEND_URL")

celery_app = Celery(__name__, broker=BROKER_URL, backend=BACKEND_URL, include=["celery_tasks.tasks"])
mongodb_backend_settings = {
    'database': 'watchcord',
    'taskmeta_collection': 'celery_backend',
}
celery_app.conf.update(
    result_backend='mongodb',
    result_backend_settings=mongodb_backend_settings,
    timezone='Asia/Kolkata',
    enable_utc=True,
)