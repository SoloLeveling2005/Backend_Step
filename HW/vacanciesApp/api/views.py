from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VacanciesSerializer
from .models import Vacancies


# Create your views here.

@api_view(['GET'])
def vacancies(request):
    """Просмотр списка вакансий."""
    all_vacancies = Vacancies.objects.all()
    return Response(data=VacanciesSerializer(all_vacancies, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def detail(request, vacancy_id: int):
    """Детальный просмотр вакансии."""
    vacancy = Vacancies.objects.filter(id=vacancy_id)
    if not vacancy.exists():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(data=VacanciesSerializer(vacancy.first()).data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    """Создание новой вакансии."""
    title = request.POST['title']
    description = request.POST['description']
    rate = request.POST['rate']

    if not title or not description or not rate:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    vacancy = Vacancies.objects.create(title=title, description=description, rate=rate)
    return Response(data=VacanciesSerializer(vacancy).data, status=status.HTTP_201_CREATED)
