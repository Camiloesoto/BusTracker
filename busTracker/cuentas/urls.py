from django.shortcuts import render
from django.urls import path

from . import views

urlpatterns = [
    path('signupaccount/', views.signupaccount,
         name='signupaccount'),
    path('home/', views.home, name='home'),
    path('login/', views.loginaccount, name='loginaccount')
]
