from datetime import datetime

import pytz
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponsePermanentRedirect
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render
# from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django_api import models
from django_api import serializers as django_serializers


@api_view(http_method_names=["GET", "PUT", "PATCH", "DELETE", "POST"])
@permission_classes((permissions.AllowAny,))
def index(request: HttpRequest,):
    if request.method == "GET":
        return render(request, 'auth.html')
    elif request.method == "POST":
        username = request.data.get("username", None)
        password = request.data.get("password", None)
