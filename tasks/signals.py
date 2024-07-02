from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from .models import Task


@receiver(post_save, sender=Task)
def send_task_notification(sender, instance, created, **kwargs):
    subject = f"Task {'Created' if created else 'Updated'} : {instance.title}"
    message = f"A New task has been {'created' if created else 'Updated'}"

    #print("New post save")

    profile = instance.profile

    send_mail(
            subject=subject,
            message=message,
            from_email="noreply@email.com",
            recipient_list=[profile.user.email],
            fail_silently=False,
            )


