from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render

# from django_api import models
# from django_api import serializers as django_serializers



def index(request):
    data = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }
    # return HttpResponse("<h1>Hello world</h1>")
    # return JsonResponse(data={
    #     "userId": 1,
    #     "id": 1,
    #     "title": "delectus aut autem",
    #     "completed": False
    # }, safe=False, content_type="application/json", indent=2)
    return JsonResponse(data=data, safe=True)





@api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE"])
def posts(request: HttpRequest, id="0") -> Response:
    id = int(id)
    return Response(data={"detail": "Successfully deleted"}, status=status.HTTP_200_OK)