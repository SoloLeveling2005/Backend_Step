from django.urls import path, include
from django_app import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("weather/", views.weather, name="weather"),
    path("money/", views.money, name="money"),
]