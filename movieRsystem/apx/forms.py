# apx/forms.py
from django import forms
from apx.models import UserProfileInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('interest',)

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password')


class InterestForm(forms.ModelForm):
    interest = forms.CharField(max_length=200)
    class Meta():
        model = User
        fields = ('interest',)