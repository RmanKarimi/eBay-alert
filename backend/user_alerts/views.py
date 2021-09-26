from .serializers import UserAlertsSerializer
from .models import UserAlerts
from rest_framework.viewsets import ModelViewSet
from user_alerts.tasks import Alert

class UserAlert(ModelViewSet):
    http_method_names= ['get', 'put', 'patch', 'delete', 'post']
    queryset = UserAlerts.objects.all()
    serializer_class = UserAlertsSerializer

    def perform_create(self, serializer):
        serializer.save()
        alert = Alert(serializer.data["id"])
        alert.send_email()
