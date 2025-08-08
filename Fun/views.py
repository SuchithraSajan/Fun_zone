from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import messages

def home(request):
    return render(request, 'home.html')



def sign(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        dob = request.POST['dob']
        gender = request.POST['gender']

        # Create the User
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Create the UserProfile
        UserProfile.objects.create(
            user=user,
            phone=phone,
            dob=dob,
            gender=gender
        )

        messages.success(request, 'Account created successfully!')
        return redirect('#')  # or your home page

    return render(request, 'signup.html')  # your signup template
