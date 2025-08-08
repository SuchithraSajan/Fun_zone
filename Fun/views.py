from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def next_page(request):
    return render(request, 'next.html')

