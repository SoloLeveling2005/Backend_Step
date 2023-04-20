import datetime
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import ProfileForm, Profile, Reviews


# Create your views here.

def main(request):
    form = ProfileForm
    users = Profile.objects.all()
    return render(request, 'main.html', context={'form': form, 'users': users})


def add_profile(request):
    username = request.POST['username']
    description = request.POST['description']
    form = Profile(username=username, description=description)
    form.save()

    return redirect('main')


def new_estimation(request):
    print(request.POST)
    estimation = request.POST['estimation']
    user = Profile.objects.get(id=request.POST['user_id'])
    Reviews(estimation=estimation, profile=user).save()
    return redirect('main')


def logout(request):
    pass


def login(request):
    message = ""
    if request.method == "POST":
        if request.POST['signup']:
            username = request.POST['username']
            description = request.POST['description']
            if Profile.objects.filter(username=username).exists():
                message = "Такой пользователь уже существует"
            else:
                token = time.time()
                Profile.objects.create(username=username, description=description, token=token)
                resp = redirect('main')
                resp.set_cookie('token', token, max_age=60 * 60)
        else:
            username = request.POST['username']
            if Profile.objects.filter(username=username).exists():
                token = time.time()
                user = Profile.objects.get(username=username)
                user.token = token
                resp = redirect('main')
                resp.set_cookie('token', token, max_age=60 * 60)
            else:
                message = "Такого пользователя не существует"
    return render(request, 'auth.html', context={'error': message})
