from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django_settings import settings
from web import views

urlpatterns = [
    # todo GET - return template, POST - auth user
    path("", views.auth, name="auth"),

    # todo GET - return template all ads
    path("home", views.home, name="home"),

    # todo GET - return template user info
    path("user/<str:user_id>", views.user, name="user"),

    # todo GET - return template one ad for edit, POST - edit this ad
    path("user/<str:user_id>/ad/<str:ad_id>", views.ad_edit, name="ad_edit"),

    # todo GET - return template one ad
    path("ad/<str:ad_id>", views.ad, name="ad"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)