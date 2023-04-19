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
    Reviews()
    return redirect('main')