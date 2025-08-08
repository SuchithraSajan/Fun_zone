from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # You can change this
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def welcome(request):
    return render(request,'welcomepage.html')