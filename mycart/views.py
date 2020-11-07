from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User



def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['passagain']:
            # check previous user
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username Already Exists.Try with a different one'})

            except user.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password'])
                return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Password does not match.Please try again.'})
    else:
        return render(request, 'signup.html')


def Login(request):
    if request.method == "POST":
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=uname, password=pwd)
        if user is not None:
            auth.login(request, user)
            return render(request, 'result.html', {'uname': uname})
        else:
            return render(request, 'login.html', {'error': 'invalid credential details'})
    else:
        return render(request, 'signup.html')


def logout(request):
    return redirect('login')
