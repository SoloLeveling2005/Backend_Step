import json
import random

from bs4 import BeautifulSoup
import requests

req = requests.get('https://world-weather.ru/pogoda/kazakhstan/astana/',headers={
"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})

soup = BeautifulSoup(req.content, 'html.parser')
# data_1 = soup.find_all(class_="weather-now-info")
# data_2 = data_1[0].find_all(id="weather-now-number")
# print(data_2[0].get_text())
data_days = soup.find_all(class_="numbers-month")
data_temp = soup.find_all(class_="day-temperature")

for i in data_days:
    print(i.getText())
for i in data_temp:
    print(i.getText())
