from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('welcome',views.welcome),
    path('login',views.signIn)
]