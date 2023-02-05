import json
import time

from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render
# from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django_api import models
from django_api import serializers as django_serializers


@api_view(http_method_names=["GET","POST","DELETE","OPTIONS"])
@permission_classes((permissions.AllowAny,))
def index(request):
    print("index")
    if request.method == "GET":
        data = models.ToDo.objects.all()
        data_json = django_serializers.ToDosSerializer(instance=data, many=True).data
        return Response(data=data_json, status=status.HTTP_200_OK)
    if request.method == "POST":
        try:
            print(request.body)
            jsonResponse = json.loads(request.body.decode('utf-8'))
            title = jsonResponse['title']
            # print(request.POST['title'])
            models.ToDo.objects.create(title=title)
            data = models.ToDo.objects.all()
            data_json = django_serializers.ToDosSerializer(instance=data, many=True).data
            return Response(data=data_json, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print('error')
            return Response(data=str(e), status=status.HTTP_204_NO_CONTENT)
    if request.method == "DELETE":
        try:
            time.sleep(4)
            print(request.body)
            jsonResponse = json.loads(request.body.decode('utf-8'))
            id_ = jsonResponse['id']
            data_model = models.ToDo.objects.get(id=id_)
            data_model.delete()
            data = models.ToDo.objects.all()
            data_json = django_serializers.ToDosSerializer(instance=data, many=True).data
            return Response(data=data_json, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print('error')
            return Response(data=str(e), status=status.HTTP_204_NO_CONTENT)

# @api_view(http_method_names=["POST", "PUT", "PATCH", "DELETE"])
# @permission_classes((permissions.AllowAny,))
# def create_todo(request, title: str):
#     data = models.ToDo.objects.create(title=title)
#     return Response(data=data, status=status.HTTP_200_OK)
