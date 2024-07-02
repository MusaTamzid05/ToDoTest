from rest_framework import serializers
from tasks.models import Task
from tasks.models import Profile
from django.contrib.auth.models import User
from tasks.celery_tasks import send_celery_task_notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ "id", "username", "email"]

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = [ "id", "user"]

class TaskSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all(), source='profile', write_only=True
    )


    class Meta:
        model = Task
        fields = ["id", "title", "description", "due_date", "status", "profile", "profile_id"]

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        send_celery_task_notification.delay(task_id=task.id, created=True)
        return task


    def update(self, instance, validated_data):
        task = super().update(instance, validated_data)
        send_celery_task_notification(task_id=task.id, created=False)
        return task
