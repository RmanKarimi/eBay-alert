from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

def update_alert():
    app.conf.update(
        imports=['user_alerts.tasks'],
        beat_schedule={
            'send_mail': {
                'task': 'user_alerts.tasks.Alert',
                'schedule': crontab(),
            },
        },
    )