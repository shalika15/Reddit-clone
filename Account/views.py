from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.


def signup(request):

    if request.method == 'POST':
        if request.POST['Password1'] == request.POST['Password2']:
            try:
                User.objects.get(username=request.POST['UserName'])
                return render(request, "Account/signup.html", {'err': "User-Id already exist"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['UserName'], password=request.POST['Password1'])
                login(request, user)
                return render(request, "Account/signup.html", {'err': "Signed-Up Successfully"})
        else:
            return render(request, "Account/signup.html", {'err': "Please confirm password"})
    else:
        return render(request, "Account/signup.html")


def logins(request):

    if request.method == 'POST':
        user = authenticate(username=request.POST['UserName'], password=request.POST['Password'])
        if user is not None:
            login(request, user)
            if request.POST.get('next1'):
                if 'next1' in request.POST:
                    return redirect(request.POST["next1"])

            return render(request, "Account/login.html", {'err': "Login-Successfully"})
        else:
            return render(request, "Account/login.html", {'err': "Invalid Id password"})

    else:
        return render(request, "Account/login.html")
