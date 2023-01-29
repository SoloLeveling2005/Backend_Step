import time

import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.core.cache import caches
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create your views here.
LocMemCache = caches["default"]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def weather(request):
    time_start = time.perf_counter()
    # cities = {
    #     'astana': 'weather-astana-5164',
    #     'almaty': 'weather-almaty-5205',
    #     'pavlodar': 'weather-pavlodar-5174'
    # }
    # city = cities[f'{city}']
    result_mass = []
    weathers = LocMemCache.get("weathers")

    if weathers is None:
        response = requests.get(f"https://www.gismeteo.kz/weather-almaty-5205/", headers=headers)
        # response = requests.get("https://www.gismeteo.kz/weather-lagos-6834/", headers=headers)
        text = response.text  # response.content.decode(encoding="utf-8")
        soup = BeautifulSoup(text, 'html.parser')
        result = soup.find_all('a', class_="weathertab weathertab-block tooltip")
        result_mass = []
        for result_one in result:
            result = result_one.find_all('span', class_="unit unit_temperature_c")
            # print(result)
            for i in result:
                result_mass.append(i.text)
        LocMemCache.set("weathers", result_mass, timeout=5)
        weathers = result_mass

    time_end = time.perf_counter()
    return render(request, "weather.html", context={"result": weathers, "time": round(time_end - time_start, 6)})
    # Без кеша запрос длиться 0,463819 секунды
    # С использованием кеша запрос длиться 0,00002 секунды

def money(request):
    time_start = time.perf_counter()

    money_ = LocMemCache.get("money_")
    if money_ is None:
        browser = webdriver.Chrome()
        browser.get('https://finance.rambler.ru/calculators/converter/1-KZT-USD/')

        usd_to_kzt_and_kzt_to_usd  = browser.find_elements(By.CLASS_NAME, 'converter-display__column')

        data = [i.text for i in usd_to_kzt_and_kzt_to_usd]
        money_ = data
        LocMemCache.set("money_", data, timeout=5)

    time_end = time.perf_counter()
    return render(request, "money.html", context={"result": money_, "time": round(time_end - time_start, 6)})