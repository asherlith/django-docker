from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
app = Celery('library')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

# using celery beat to schedule a task every 10 seconds.
app.conf.beat_schedule = {
    # any name can be chosen
    'change-the-reader': {
        # where the task is located
        'task': 'books.tasks.changeReader',
        # when it will execute
        "schedule": timedelta(seconds=10),
        # arguments passed into the task function
        'args': (20,)
    }
}
