from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('form_request', views.form_request, name='form_request'),
    path('get_urls/<int:count_>', views.get_urls, name='get_urls'),
]


