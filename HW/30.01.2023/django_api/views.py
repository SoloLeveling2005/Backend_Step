import json
import time

from django.http import HttpResponse, HttpRequest, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render
# from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django_api import models
from django_api import serializers as django_serializers


# @method_decorator(ensure_csrf_cookie, name='dispatch')
# class GetCSRFToken:
#     permissions_classes = (permissions.AllowAny, )
#
#     def get(self):
#         return Response({'success': 'CSRF Cookie set'})
#

@api_view(http_method_names=["POST", "GET", "DELETE"])
@permission_classes((permissions.AllowAny,))
def index(request):
    print("index")
    if request.method == "GET":
        data = models.ToDo.objects.all()
        data_json = django_serializers.ToDosSerializer(instance=data, many=True).data
        return Response(data=data_json, status=status.HTTP_200_OK)
    elif request.method == "POST":
        try:
            print(request.data)
            title = request.data['title']
            # print(request.POST['title'])
            models.ToDo.objects.create(title=title)
            data = models.ToDo.objects.all()
            data_json = django_serializers.ToDosSerializer(instance=data, many=True).data
            return Response(data=data_json, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print('error')
            return Response(data=str(e), status=status.HTTP_204_NO_CONTENT)
    elif request.method == "DELETE":
        try:
            print(request.data)
            id_ = request.data['id']
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

