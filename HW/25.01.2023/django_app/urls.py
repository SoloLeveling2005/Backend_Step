from django.urls import path, include
from django_app import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("index/<str:city>", views.index, name="index"),
]