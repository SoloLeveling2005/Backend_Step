from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('index/', views.index, name='user'),
    path('form_request/', views.form_request, name='login'),
]


