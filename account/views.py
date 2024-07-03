from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponse
from .forms import LoginForm
from .forms import UserRegistrationForm
from .models import Profile
from tasks.models import Task
from account.models import Profile




@login_required
def dashboard(request):
    username = request.user.username
    profile = Profile.objects.get(user=request.user)

    status_filter = request.GET.get("status", "")

    if status_filter:
        tasks = Task.objects.filter(profile=profile, status=status_filter)
    else:
        tasks = Task.objects.filter(profile=profile)

    sort_order = request.GET.get("sort", "created_at")


    if sort_order == "due_date":
        tasks = tasks.order_by("due_date")
    else:
        tasks = tasks.order_by("created_at")


    return render(
            request,
            "account/dashboard.html",
            {"username" : username, "tasks" : tasks,
                "status_filter" : status_filter, 
                "sort_order" :sort_order 
            }


            )


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=True)
            new_user.set_password(user_form.cleaned_data["password"])

            new_user.save()
            Profile.objects.create(user=new_user)

            return render(
                    request,
                    "account/register_done.html",
                    {"new_user" : new_user}
                    )
    else:
        user_form = UserRegistrationForm()

    return render(
            request,
            "account/register.html",
            {"user_form" : user_form}
            )

