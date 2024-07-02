from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from account.models import Profile
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from .celery_tasks import send_celery_task_notification


@login_required
def create_task(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.profile = profile
            task.save()
            send_celery_task_notification.delay(task_id=task.id, created=True)
            return redirect("dashboard")
    else:
        form = TaskForm()

    return render(request, "tasks/create_task.html", {"form" : form})



@login_required
def delete_task(request, task_id):
    profile = Profile.objects.get(user=request.user)
    task = get_object_or_404(Task,id=task_id, profile=profile)


    if request.method == "POST":
        task.delete()
        return redirect("dashboard")

    return render(request, "tasks/delete_task.html", {"task" : task})





@login_required
def edit_task(request, task_id):
    profile = Profile.objects.get(user=request.user)
    task = get_object_or_404(Task,id=task_id, profile=profile)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task = form.save()
            send_celery_task_notification.delay(task_id=task.id, created=False)
            return redirect("dashboard")
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/edit_task.html", {"form" : form})


@login_required
def show_task(request, task_id):
    profile = Profile.objects.get(user=request.user)
    task = get_object_or_404(Task,id=task_id, profile=profile)

    return render(request, "tasks/show_task.html", {"task" : task})
