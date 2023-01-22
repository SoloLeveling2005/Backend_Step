from datetime import datetime

import pytz
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponsePermanentRedirect
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render, redirect
# from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from authentication import models
# from django_api import serializers as django_serializers


@api_view(http_method_names=["GET", "PUT", "PATCH", "DELETE", "POST"])
@permission_classes((permissions.AllowAny,))
def index(request: HttpRequest,):
    if request.method == "GET":
        return render(request, 'auth.html')
    elif request.method == "POST":
        username = request.data.get("username", None)
        password = request.data.get("password", None)

        reg = request.data.get("reg", None)
        auth = request.data.get("auth", None)


        if username is None or password is None:
            return render(request, 'auth.html')
        elif reg is not None:
            print("1")
            print(username)
            print(password)
            new_data_in_db = models.Users.objects.create(
                username=username,
                password=password
            )
            new_data_in_db.save()
            print("1.1")
            # user = models.Users.objects.get(username=username, password=password)
            return redirect(reverse('django_app:index', kwargs={"user_id": new_data_in_db.id}))
        elif auth is not None:
            print("2")
            try:
                user = models.Users.objects.get(username=username, password=password)
                return redirect(reverse('django_app:index', kwargs={"user_id": user.id}))
            except Exception as e:
                print(e)
        else:
            return render(request, 'auth.html')
