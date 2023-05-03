from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .models import User, Post, Comment


# Create your views here.


def index(request):
    print("123")
    if request.COOKIES.get('user_id'):

        return render(request, 'index.html')
    else:
        return redirect('app:auth')


def auth(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user_id = User.create_user(username=username, password=password)
            req = redirect('app:index')
            req.set_cookie('user_id', user_id)
            return req

    return render(request, 'auth.html')


def home_(request):
    return render(request, 'home.html')


class Home(TemplateView):
    template_name = "home.html"