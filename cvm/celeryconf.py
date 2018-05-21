import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cvm.settings')

app = Celery('cvm')

CELERY_TIMEZONE = 'Asia/Seoul'

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
