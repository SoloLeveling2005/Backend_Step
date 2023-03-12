from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from web import models


# Create your views here.


def index(request):
    data = models.Post.objects.all()
    print(data)
    return render(request, 'index.html', context={'data': data})


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
