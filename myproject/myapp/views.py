from django.shortcuts import render, redirect
from myapp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def signup (request):
    if request.method == 'POST':
        userType = request.POST.get('userType')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        gender = request.POST.get('gender')
        education = request.POST.get('education')

        if (password == confirmPassword):
            user = CustomUserModel.objects.create_user(username=username, password=confirmPassword)
            user.first_name = fname
            user.last_name = lname
            user.email = email
            user.UserType = userType
            user.Gender = gender
            user.Education = education

            user.save()
            messages.success(request, "Registration successful!")
            return redirect('signin')
        else:
            messages.error(request, "Passwords do not match!")
            return redirect('signin')
    return render (request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            # display error message
            messages.error(request, "Invalid Password")
            return redirect('signin')
        else:
            login(request, user)
            return redirect('dashboard')

    return render (request, 'signin.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')



def signout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('signin')