from django.shortcuts import render

# Create your views here.


def index(request):
    return "Index"


def form_request(request):
    return {"info": 'form request'}