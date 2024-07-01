from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponse
from .forms import LoginForm



@login_required
def dashboard(request):
    return render(
            request,
            "account/dashboard.html"
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

