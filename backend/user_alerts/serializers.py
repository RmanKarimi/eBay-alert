from rest_framework import serializers
from .models import UserAlerts, EbayItems

class UserAlertsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserAlerts
        fields= "__all__"

class EbayCardItemsSerializer(serializers.ModelSerializer):
    class Meta:
        models=EbayItems
        fields= "__all__"
