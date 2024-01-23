from celery import Celery

app = Celery('tasks')
app.config_from_object("celeryconfig")
app.conf.imports = ('firstapp.tasks')
app.autodiscover_tasks()
