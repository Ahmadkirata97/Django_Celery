import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcalaries.settings')
app = Celery("dcalaries")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.task_routes = {
    'firstapp.tasks.*': {'queue':'q1'},
    'firstapp.tasks.task2': {'queue':'q2'},
}



app.autodiscover_tasks()