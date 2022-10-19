import time

import requests
from bs4 import BeautifulSoup
import random
import threading
response = requests.get('https://picsum.photos/',
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    })

# time.sleep(1)
if response.status_code == 200:
    def start_download(i):
        print('Success!')
        soup = BeautifulSoup(response.content, "html.parser")
        tags = soup.find_all("img")
        key = soup.select_one("img-responsive")
        url = f"https://picsum.photos/{tags[i]['src']}"
        img_data = requests.get(url).content
        with open(f'image_name{i}.jpg', 'wb') as handler:
            handler.write(img_data)
    for i in range(3):
        t = threading.Thread(target=start_download, args=(i+1,))
        t.start()