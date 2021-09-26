from django.urls import include, path
from rest_framework import routers
from .views import UserAlert

router = routers.DefaultRouter()
router.register('', UserAlert)

urlpatterns = [
    path('', include(router.urls)),
]