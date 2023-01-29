import requests
from django.shortcuts import render
from django.core.cache import caches

# Create your views here.
LocMemCache = caches["special"]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}

def index(request, city: str):
    cities = {
        'astana': 'weather-astana-5164',
        'almaty': 'weather-almaty-5205',
        'pavlodar': 'weather-pavlodar-5174'
    }
    city = cities[f'{city}']
    response = requests.get(f"https://www.gismeteo.kz/{city}/", headers=headers)
    # response = requests.get("https://www.gismeteo.kz/weather-lagos-6834/", headers=headers)
    text = response.text  # response.content.decode(encoding="utf-8")

    return render(request, "weather.html", context={"result": result})
