from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from Core.views import home
from django.contrib import messages

# Create your views here.
def singin(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in!!")
        return redirect(home)
    
    if  request.method == "POST":
        username = request.POST['signin_username']
        password = request.POST['signin_password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect(reverse('admin:index'))
            else:
                messages.success(request, "You are successfully logged in!!")
                return redirect(home)
        else:
            error_message = "User not found!! Provide valid credintials."
            return render(request, "authentication/signin.html", {'error_message': error_message})
    return render(request, "authentication/signin.html")



def singup(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already user!!")
        return redirect(home)

    if  request.method == "POST":
        username = request.POST['signup_username']
        email = request.POST['signup_email']
        pass1 = request.POST['signup_password']
        pass2 = request.POST['signup_confirm_password']

        if not username or not email or not pass1 or not pass2:
                error_message = "Please fill up all feilds!!"
                return render(request, "authentication/signup.html", {'error_message': error_message})
        if pass1 != pass2:
            error_message = "Password does not match!!"
            return render(request, "authentication/signup.html", {'error_message': error_message})
        elif User.objects.filter(username=username).exists():
            error_message = "Username already exists!!"
            return render(request, "authentication/signup.html", {'error_message': error_message})
        elif User.objects.filter(email=email).exists():
            error_message = "Email already exists!!"
            return render(request, "authentication/signup.html", {'error_message': error_message})
        else:
            user = User.objects.create_user(username=username, email=email, password=pass1)
            user.save()
            messages.success(request, "Your account successfully created!!")
            return redirect(singin)
    
    return render(request, "authentication/signup.html")


def signout(request):
    logout(request)
    messages.warning(request, "Your are now logged out!!")
    return redirect(singin)