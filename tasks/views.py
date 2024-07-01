from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from account.models import Profile
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required


@login_required
def create_task(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.profile = profile
            task.save()
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



