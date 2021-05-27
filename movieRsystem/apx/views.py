from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from apx.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def home(request):
    return render(request, 'home.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'register.html',
                          {'user_form':user_form,
                           'registered':registered})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home.html'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})
    

@login_required
def dashboard(request):

    return render(request, 'dashboard.html')

@login_required
def dashboard(request):
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(data=request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.interest = interest
            profile.save()
        else:
            print(profile_form.errors)
    else:
        profile_form = UserProfileInfoForm()

    return render(request,'dashboard.html',
                          {'profile_form':profile_form, 'user':user,'interest':interest,})
