import django
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from apx.forms import UserForm,UserProfileInfoForm, LoginForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from apx.models import UserProfileInfo, User, userMovieWatched, moviesData, moviesgenre



def home(request):
    return render(request, 'home.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    # registered = False
    # if request.method == 'POST':
    #     user_form = UserForm(data=request.POST)
    #     if user_form.is_valid():
    #         user = user_form.save()
    #         user.set_password(user.password)
    #         user.save()

    #         registered = True
    #     else:
    #         print(user_form.errors)
    # else:
    #     user_form = UserForm()
    # return render(request,'register.html',
    #                       {'user_form':user_form,
    #                        'registered':registered})
    
# def RegisterPage(request):
	if request.user.is_authenticated:
		return redirect('apx/dashboard')
	else:
		form = UserForm()
		if request.method == 'POST':
			form = UserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				# messages = "Account was created for " + user
				return redirect('userlogin')
            
		context = {'form':form}
		return render(request,'register.html',context)

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('apx/dashboard')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username =  form.cleaned_data.get('username')
                password =  form.cleaned_data.get('password')
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('apx/dashboard')
                # else:
                    # messages.info(request,'Username or password is incorrect')
        # context = {}
    return render(request,'login.html')
        
    
    

def dashboard(request):

    dataPreffb = UserProfileInfo.objects.all()



    stu = {
    "dataPref": dataPreffb
    }


    return render(request, 'dashboard.html', stu)


# def dashboard(request):
#     if request.method == 'POST':
#         profile_form = UserProfileInfoForm(data=request.POST)
#         if profile_form.is_valid():
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.interest = interest
#             profile.save()
#         else:
#             print(profile_form.errors)
#     else:
#         profile_form = UserProfileInfoForm()

#     return render(request,'dashboard.html',
#                           {'profile_form':profile_form, 'user':user,'interest':interest,})
