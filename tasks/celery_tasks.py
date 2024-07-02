from celery import shared_task
from django.core.mail import send_mail
from .models import Task


@shared_task
def send_celery_task_notification(task_id, created):
    task = Task.objects.get(id=task_id)
    profile = task.profile

    subject = f"Task {'Created' if created else 'Updated'} : {task.title}"
    message = f"A New task has been {'created' if created else 'Updated'}"




    send_mail(
            subject=subject,
            message=message,
            from_email="noreply@email.com",
            recipient_list=[profile.user.email],
            fail_silently=False,
            )

