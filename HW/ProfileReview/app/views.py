from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import ProfileForm, Profile, Reviews
from uuid import uuid4

# Create your views here.

def main(request):
    username = request.COOKIES.get('username')
    if not username:
        return redirect('add_profile')

    form = ProfileForm
    users = Profile.objects.all()
    user_profile = Profile.objects.get(username=username)
    user_estimations = Reviews.objects.filter(profile=user_profile)
    users_estimations = [user.estimations() for user in users]
    for i in users_estimations:
        for x in i.all():
            print(x.profile.username)
    return render(request, 'main.html', context={'form': form, 'users': users,
                                                 'user_estimations': user_estimations, 'username': username})


def add_profile(request):
    if request.method == "POST":
        username = request.POST.get('username')
        description = request.POST.get('description')
        form = Profile(username=username, description=description)
        form.save()
        response = redirect('main')
        response.set_cookie('username', username)
        return response
    else:
        username = request.COOKIES.get('username')
        if username:
            return redirect('main')
        return render(request, 'login.html', context={})


def new_estimation(request):
    username = request.COOKIES.get('username')
    if not username:
        return redirect('add_profile')

    print(request.POST)
    estimation = request.POST.get('estimation')
    user = Profile.objects.get(username=username)
    Reviews(estimation=estimation, profile=user).save()
    return redirect('main')
