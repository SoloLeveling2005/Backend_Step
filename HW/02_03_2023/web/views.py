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
    data = models.Post.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        token = time.time() + random.randint(100, 999)

        if models.User.objects.filter(username=username).exists():
            return render(request, 'index.html', context={'error': 'Такой пользователь уже существует', 'user': ""})
        else:
            models.User.objects.create(username=username, password=make_password(password), token=token)

        user = models.User.objects.get(token=token)

        rendered_view = render(request, 'index.html', context={'data': data, 'user': user})
        rendered_view.set_cookie('token', token)
        return rendered_view
    else:
        try:
            user = models.User.objects.get(token=token) if models.User.objects.filter(token=token).exists() else ""
        except Exception as e:
            rendered_view = render(request, 'index.html', context={'user': ""})
            return rendered_view

        if user == "":
            rendered_view = render(request, 'index.html', context={'user': user})
            return rendered_view


        rendered_view = render(request, 'index.html', context={'data': data, 'user': user})
        return rendered_view


def new_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        user_id = request.POST['user_id']
        user = models.User.objects.get(id=user_id)

        models.Post.objects.create(title=title, description=description, user=user)

    return HttpResponseRedirect(reverse('index'))


def post_like(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        user_id = request.POST['user_id']
        user = models.User.objects.get(id=user_id)

        try:
            post = models.Post.objects.get(id=post_id)

            try:
                like = models.Like.objects.get(post=post, user=user)
                like.delete()
            except Exception as e:
                print(e)
                models.Like.objects.create(post=post, user=user)
        except Exception as e:
            print(e)

    return HttpResponseRedirect(reverse('index'))


def post_comment(request):
    post_id = request.POST['post_id']
    text = request.POST['text']
    user_id = request.POST['user_id']
    user = models.User.objects.get(id=user_id)

    try:
        post = models.Post.objects.get(id=post_id)
        models.Comment.objects.create(text=text, post=post, user=user)
    except Exception as e:
        print(e)

    return HttpResponseRedirect(reverse('index'))
