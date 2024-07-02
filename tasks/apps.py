from django.apps import AppConfig
from django.db.models.signals import post_save


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        from .signals import send_task_notification
        post_save.connect(send_task_notification, sender="tasks.Task")
        
