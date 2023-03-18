import random
import time

from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from web import models


# Create your views here.


def index(request):
    token = request.COOKIES.get('token')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        token = time.time() + random.randint(100, 999)

        if models.User.objects.filter(username=username).exists():
            return render(request, 'index.html', context={'error': 'Такой пользователь уже существует'})
        else:
            models.User.objects.create(username=username, password=make_password(password), token=token)

        user = models.User.objects.get(token=token)

        rendered_view = render(request, 'index.html', context={'user': user})
        rendered_view.set_cookie('token', token)
        return rendered_view
    else:
        print(models.User.objects.filter(token=token).exists())
        try:
            user = models.User.objects.get(token=token) if models.User.objects.filter(token=token).exists() else ""
        except Exception as e:
            rendered_view = render(request, 'index.html', context={'user': ""})
            return rendered_view

        if user == "":
            rendered_view = render(request, 'index.html', context={'user': user})
            return rendered_view

        data = models.Post.objects.all()
        rendered_view = render(request, 'index.html', context={'data': data, 'user': user})
        return rendered_view


def new_post(request):
    title = request.POST['title']
    description = request.POST['description']
    models.Post.objects.create(title=title, description=description)

    return HttpResponseRedirect(reverse('index'))


def post_like(request):
    post_id = request.POST['post_id']
    post = models.Post.objects.get(id=post_id)
    models.Like.objects.create(post_id=post)
    return HttpResponseRedirect(reverse('index'))


def post_comment(request):
    post_id = request.POST['post_id']
    text = request.POST['text']
    post = models.Post.objects.get(id=post_id)
    models.Comment.objects.create(text=text, post_id=post)
    return HttpResponseRedirect(reverse('index'))
