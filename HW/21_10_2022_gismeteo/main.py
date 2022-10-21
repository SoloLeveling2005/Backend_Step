from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__, template_folder='templates')


@app.route("/")
def get_weather():
    mass_data_days = []
    mass_data_temp = []
    req = requests.get('https://world-weather.ru/pogoda/kazakhstan/astana/', headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})

    soup = BeautifulSoup(req.content, 'html.parser')

    data_days = soup.find_all(class_="numbers-month")
    data_temp = soup.find_all(class_="day-temperature")

    for i in data_days:
        mass_data_days.append(i.getText())
    for i in data_temp:
        mass_data_temp.append(i.getText())

    return render_template('get_weather.html', mass_data_days=mass_data_days, mass_data_temp=mass_data_temp)
