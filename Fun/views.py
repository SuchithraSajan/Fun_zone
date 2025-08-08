from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=name).exists():
            return render(request, 'signup.html', {'error': 'Username already taken'})

        user = User.objects.create_user(username=name, email=email, password=password)
        login(request, user)
        return redirect('success')  

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('first')  
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def success_page(request):
    return render(request, 'success.html')

def first(request):
    return render(request,'first.html')

def neon(request):
    return render(request,'neon.html')

def prank(request):
    return render(request,'prank.html')

def chik(request):
    return render(request,'chik.html')

def t_or_d(request):
    return render(request,'t_or_d')
