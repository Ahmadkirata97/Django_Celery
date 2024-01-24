import os
from celery import Celery
from kombu import Queue, Exchange
import time 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcalaries.settings')
app = Celery("dcalaries")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]

app.conf.task_acks_late = True # Sets the late Ack of tasks, execute the task then send Ack 
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1 # enable the worker to fetch multiple tasks from the broker at once 
app.conf.worker_concurrency = 1 # number of worker threds that celery will reserve to process task 

@app.task(queue='tasks')
def t1():
    time.sleep(10)
    return 

@app.task(queue='tasks')
def t2():
    time.sleep(10)
    return 

@app.task(queue='tasks')
def t3():
    time.sleep(10)
    return 

@app.task(queue='tasks')
def t4():
    time.sleep(10)
    return 


# app.conf.task_routes = {
#     'firstapp.tasks.*': {'queue':'q1'},
#     'firstapp.tasks.task2': {'queue':'q2'},
# }

# app.conf.task_default_rate_limit = '1/m'


# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep':':',
#     'queue_order_strategy':'priority',
# }



app.autodiscover_tasks()