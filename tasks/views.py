from django.shortcuts import render
from django.shortcuts import redirect
from account.models import Profile
from .forms import TaskForm
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



