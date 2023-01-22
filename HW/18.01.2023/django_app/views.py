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
def index(request: HttpRequest, id=-1, user_id=-1):
    if user_id != -1:
        if id == -1:
            task = models.Tasks.objects.filter(user_id=user_id)  # TODO QuerySet != JSON
            print(task)
            data_json = django_serializers.PostsSerializer(instance=task, many=True)
            return render(request, 'index.html', context={"todos": task})
        else:
            if request.method == "GET":
                try:
                    task = models.Tasks.objects.filter(id=id)
                    print('task', task)
                    data_json = django_serializers.PostsSerializer(instance=task, many=True)
                    return Response(data=data_json.data, status=status.HTTP_200_OK)
                except Exception as e:
                    print(e)
                    return Response(data={"error": f"Данных не существует"}, status=status.HTTP_204_NO_CONTENT)
    else:
        return HttpResponsePermanentRedirect("/")