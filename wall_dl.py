#! /usr/bin/python3

import requests
import sys
import os
import string
import random

def wallpaper_search(query):
    url = f"https://wallhaven.cc/api/v1/search?q={query}&apikey=X4aaKqQRC1oO1z8sxWsWaMSGcSbhqG1b&sorting=random"
    res = requests.get(url)

    json_data = res.json()
    dl_link=[]
    for wallpapers in json_data["data"]:
        dl_link.append(wallpapers["path"])

    return dl_link


def generate_id():
    return ''.join(random.choices(string.ascii_lowercase+string.digits, k=6))


def download_wallpaper(url):
    print(f"Downloading... {url}")
    res = requests.get(url)
    file_name = generate_id()
    ext = os.path.splitext(url)[1]
    dl_path = f"./wall_dl/{file_name}{ext}"
    open(dl_path, 'wb+').write(res.content)

key = sys.argv[1:]

waldlurl = wallpaper_search(key)

for walls in waldlurl:
    download_wallpaper(walls)

