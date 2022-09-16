import json

import requests

url = "https://jsonplaceholder.typicode.com/photos/"

json_list = []

for i in range(1,11):
    req = requests.get(f"{url}{i}")

    print(req.json())
    json_list.append(req.json())

print(json_list)