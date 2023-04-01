import asyncio
import io

import aiohttp
from asgiref.sync import sync_to_async
from bs4 import BeautifulSoup
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
# Create your views here.
import requests
import zipfile
from .models import Urls
from django.utils import timezone


def get_images_url(count_img_download):
    # смотрим есть ли достаточно ссылок фоток в бд, если есть то отправляем их иначе делаем новый запрос
    # это глупо конечно, но ничего лучше к сожалению не придумал
    count_in_model = Urls.objects.count()
    if count_in_model >= count_img_download:
        random_objects = Urls.objects.order_by('?')[:count_img_download]
        return [row.url for row in random_objects]
    else:
        parse_images_url = parse_website('https://fonwall.ru/')[1:int(count_img_download) + 1]
        data = [Urls.objects.create(url=i) for i in parse_images_url]

        return parse_images_url

def index(request):
    return HttpResponse(render(request, 'index.html'))


# Парсим сайт и собираем оттуда ссылки
def parse_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    return [img.get('src') for img in images if img.get('src')]


# Скачиваем картинки по ссылкам (асинхронно)
async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            image_data = await response.read()
            return image_data


async def form_request(request):
    if request.method == "POST":
        count_img_download = 20 if int(request.POST['count']) > 20 else int(request.POST['count'])

        images_url = await sync_to_async(get_images_url)(count_img_download)

        tasks = [asyncio.ensure_future(download_image(url)) for url in images_url]
        image_list = await asyncio.gather(*tasks)

        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, mode='w') as zip_file:
            for i, image in enumerate(image_list):
                zip_file.writestr(f'image{i + 1}.jpg', image)

        response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="images.zip"'
        return response

    return JsonResponse({'error': 'Method not allowed'})


def get_urls(request, count_):
    if request.method == "GET":
        count_img_download = 20 if int(count_) > 20 else int(count_)
        images_url = get_images_url(count_img_download)
        return JsonResponse({'imgs': images_url})
    return JsonResponse({'error': 'Method not allowed'})
