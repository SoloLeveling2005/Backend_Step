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
    profiles = Profile.objects.all()
    user = Profile.objects.get(username=username)
    profiles_reviews = [profile.estimations() for profile in profiles]
    # Конструкция не очень, потом заменю 😅
    # {1:{profile:profile, estimations:[], my_estimation:False}}
    new_profiles = {}
    for profile in profiles:
        id_ = profile.id
        print(id_)
        new_profiles[id_] = {'profile': profile, 'estimations': [], 'my_estimation': False}
        for estimation in profile.estimations():
            new_profiles[id_]['estimations'].append(estimation)
            if estimation.user == user:
                new_profiles[id_]['my_estimation'] = True
    print(new_profiles)
    return render(request, 'main.html',
                  context={'form': form, 'profiles': profiles, 'new_profiles': new_profiles,
                           'user': user})


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
    profile_id = request.POST.get('profile')
    profile = Profile.objects.get(id=profile_id)
    user = Profile.objects.get(username=username)
    estimation = request.POST.get('estimation')
    Reviews(estimation=estimation, profile=profile, user=user).save()
    return redirect('main')
