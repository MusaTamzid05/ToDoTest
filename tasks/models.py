from django.db import models
from django.utils import timezone
from account.models import Profile


class Task(models.Model):
    STATUS_CHOICES = [
            ("TO_DO", "To Do"),
            ("IN_PROGRESS", "In Progress"),
            ("DONE", "Done")
            ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="task")
    title = models.CharField(max_length=2000)
    description = models.TextField()
    due_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(
            max_length=20,
            choices=STATUS_CHOICES,
            default="TO_DO"
            )

    def __str__(self):
        return self.title
