from django.urls import path
from django.urls import include
from rest_framework.routers  import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
        path("", include(router.urls)),
        ]
