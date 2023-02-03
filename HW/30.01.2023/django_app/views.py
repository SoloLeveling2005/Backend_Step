from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from django.shortcuts import render
# from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django_api import models
# from django_api import serializers as django_serializers


# @api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE"])
# @permission_classes((permissions.AllowAny,))
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
    # return Response(data=data, status=status.HTTP_200_OK)
    return render(request, "build/index.html", context=data)
# @api_view(('GET',))
# @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
# def index(request):
#     data = {
#         "userId": 1,
#         "id": 1,
#         "title": "delectus aut autem",
#         "completed": False
#     }
#     return Response(data, template_name='build/index.html')

