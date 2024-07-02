from django.shortcuts import render
from rest_framework import viewsets
from tasks.models import Task
from tasks.models import Profile
from .serializers import TaskSerializer
from .serializers import ProfileSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


