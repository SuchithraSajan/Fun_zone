from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sign(request):
    return render(request, 'signin.html')

