from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import LoginForm
from .forms import UserRegistrationForm
from .models import Profile



@login_required
def dashboard(request):
    username = request.user.username

    return render(
            request,
            "account/dashboard.html",
            {"username" : username}
            )

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            user = authenticate(
                    request,
                    username=cd["username"],
                    password=cd["password"],
                    )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("dashboard")
                else:
                    return HttpResponse("Disable Account")
            else:
                print("Invalid Login")
                return HttpResponse("Invalid Login")

        else:
            print("Form is not valid")

    else:
        form = LoginForm()




    return render(
            request,
            "account/login.html",
            {"form" : form}
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

