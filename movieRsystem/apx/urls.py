# apx/urls.py
from django.conf.urls import url
from django.urls.conf import path
from apx import views

# SET THE NAMESPACE!
app_name = 'apx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    # url(r'^register/$',views.register,name='register'),
    # url(r'^user_login/$',views.user_login,name='user_login'),
    path('register/', views.register, name='register'),
    path('userlogin/', views.login,  name='userlogin'),
    path('dashboard/', views.dashboard, name='dashboard')

]
