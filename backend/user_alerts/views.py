from .serializers import UserAlertsSerializer
from .models import UserAlerts
from rest_framework.viewsets import ModelViewSet
from user_alerts.tasks import create_alert
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import datetime

class UserAlert(ModelViewSet):
    http_method_names= ['get', 'put', 'patch', 'delete', 'post']
    queryset = UserAlerts.objects.all()
    serializer_class = UserAlertsSerializer

    def perform_create(self, serializer):
        serializer.save()
        create_alert(serializer.data["id"])
        # alert = Alert(serializer.data["id"])
        #
        # schedule = CrontabSchedule.objects.filter(minute='*/1')
        # if schedule:
        #     schedule = schedule[0]
        # else:
        #     schedule = CrontabSchedule.objects.create(minute='*/1')
        # task_name = "%s_%s" % (str(serializer.data["email"]), datetime.datetime.now())
        # task = PeriodicTask.objects.create(name=task_name,
        #                                    task='user_alerts.tasks.test', crontab=schedule)
        # task.save()

