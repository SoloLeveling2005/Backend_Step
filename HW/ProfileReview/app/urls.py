
from django.contrib import admin
from django.urls import path, include
from app import views
urlpatterns = [
    path('', views.main, name="main"),
    path('add_profile', views.add_profile, name="add_profile"),
    path('new_estimation', views.new_estimation, name="new_estimation"),

    path('logout', views.logout, name="logout"),
    path('login', views.login, name="login"),

]
