import random
import time

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from web import models


# Create your views here.


def index(request):
    return "Index"


# todo Готово
def auth(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        token = time.time() + random.randint(100, 999)

        # todo проверяем на существование пользователя с такими данными, если возникла ошибка значит регистрируем пользователя
        try:
            models.User.objects.get(username=username, password=password)
            rendered_view = render(request, 'auth.html', context={'error': 'Такой пользователь уже существует'})
            return rendered_view

        except Exception as e:
            print(e)
            models.User.objects.create(username=username, password=password, token=token)

            rendered_reverse = HttpResponseRedirect(reverse('home'))
            rendered_reverse.set_cookie('token', token)
            return rendered_reverse

    rendered_view = render(request, 'auth.html', context={})
    return rendered_view


def home(request):
    # token = request.COOKIES.get('token')
    # # todo Проверяем авторизацию пользователя
    # try:
    #     user = models.User.objects.get(token)
    # except Exception as e:
    #     print(e)
    #     rendered_reverse = HttpResponseRedirect(reverse('auth'))
    #     return rendered_reverse

    ads = models.Ad.objects.all()
    rendered_view = render(request, 'home.html', context={'ads': ads, 'user': user})
    return rendered_view


def user(request):
    token = request.COOKIES.get('token')
    # todo Проверяем авторизацию пользователя
    try:
        user = models.User.objects.get(token)
    except Exception as e:
        print(e)
        rendered_reverse = HttpResponseRedirect(reverse('auth'))
        return rendered_reverse


    rendered_view = render(request, 'user.html', context={'user': user})
    return rendered_view


def ad_edit(request):
    # token = request.COOKIES.get('token')
    # # todo Проверяем авторизацию пользователя
    # try:
    #     user = models.User.objects.get(token)
    # except Exception as e:
    #     print(e)
    #     rendered_reverse = HttpResponseRedirect(reverse('auth'))
    #     return rendered_reverse

    rendered_view = render(request, 'ad.html', context={})
    return rendered_view


def ad(request, ad_id):
    # token = request.COOKIES.get('token')
    # # todo Проверяем авторизацию пользователя
    # try:
    #     user = models.User.objects.get(token)
    # except Exception as e:
    #     print(e)
    #     rendered_reverse = HttpResponseRedirect(reverse('auth'))
    #     return rendered_reverse

    rendered_view = render(request, 'ad.html', context={})
    return rendered_view
