from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
# Create your views here.


def index(request):
    return HttpResponse(render(request, 'index.html'))


def form_request(request):
    if request.method == "POST":
        count_img_download = 123
        import requests
        from bs4 import BeautifulSoup

        def parse_website(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            images = soup.find_all('img')
            links = []
            for img in images:
                link = img.get('src')
                if link:
                    links.append(link)
            return links
        url = 'https://img3.fonwall.ru/o/dv/ferrari-f355-ferrari-cars.jpeg?route=thumb&h=350'
        image = urllib.request.urlopen(url)
        response = FileResponse(image)
        response['Content-Type'] = 'image/png'
        response['Content-Disposition'] = 'attachment; filename="image.png"'
        return response

    return JsonResponse({'error': 'Method not allowed'})
