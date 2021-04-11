from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        # User wants to sign up
        if request.POST['password1'] \
            == request.POST['password1']:
                User.objects.get(
                    username=request.POST['username'])
    else:
        # User wants to enter info
        pass
    return render(request, "accounts/signup.html")


def login(request):
    return render(request, "accounts/login.html")


def logout(request):
    # TODO: Need to route to hompage
    # and don't forget to logout.
    return render(request, "accounts/logout.html")