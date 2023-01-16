import json

from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render
# from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django_app import serializers as django_serializers


def index(request):
    context = {}
    return render(request, "index.html", context=context)


@api_view(http_method_names=["GET", "PUT", "PATCH", "DELETE"])
@permission_classes((permissions.AllowAny,))
def get_book(request, book_id: str = "-1"):
    book_id = int(book_id)
    if book_id < 0:
        data = requests.get(f"http://127.0.0.1:5000/api/get_all_books").json()
        # print(data)
        return Response(data=data, status=status.HTTP_200_OK)
    else:
        data = requests.get(f"http://127.0.0.1:5000/api/get_book/{book_id}").json()
        # print(data)
        return Response(data=data, status=status.HTTP_200_OK)
    # data = requests.get(f"http://127.0.0.1:8001/api/v2/users/{pk}")

