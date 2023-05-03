from django.contrib import admin
from django.urls import path, include, re_path
from app import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name="index"),
    path('auth', views.auth, name="auth"),
]
