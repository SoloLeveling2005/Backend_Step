import json

from django.http import JsonResponse
from django.shortcuts import render

from api.models import Book


# Create your views here.


def getDB(requests):
    data = [{'id': x.id, 'title': x.title} for x in Book.objects.all()]
    return JsonResponse(data=data, safe=False, status=202)


def postDB(requests):
    try:
        title = requests.POST.get('title')
        Book.objects.create(title=title)
        return JsonResponse({'status': 'ok'}, status=200)
    except Exception as e:
        return JsonResponse({'error': e}, status=204)


def updateDB(requests):
    try:
        book_id = requests.POST.get('id')
        book = Book.objects.get(id=int(book_id))
        book.title = "Джек Лондон"
        book.save()
        return JsonResponse({'status': 'ok'}, status=200)
    except Exception as e:
        print(e)
        return JsonResponse({'error': 'Нет данных'}, status=204)


def deleteDB(requests):
    try:
        book_id = requests.POST.get('id')
        Book.objects.get(id=int(book_id)).delete()
        return JsonResponse({'status': 'ok'}, status=200)
    except Exception as e:
        print(e)
        return JsonResponse({'error': 'Нет данных'}, status=204)
