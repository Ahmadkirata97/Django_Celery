from celery import shared_task
import time

@shared_task
def task1(queue='celery'):
    time.sleep(10)
    return

@shared_task
def task2(queue='celery:1'):
    time.sleep(10)
    return

@shared_task
def task3(queue='celery:2'):
    time.sleep(10)
    return

@shared_task
def task4(queue='celery:3'):
    time.sleep(10)
    return