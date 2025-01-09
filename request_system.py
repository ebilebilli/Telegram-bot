import requests
import os
from settings import API_KEY, SITE_URL

def request_system(category_name):
    site_url = SITE_URL
    params = {
        'q': category_name,
        'apikey': API_KEY,
        'categories': '100',
        'purity': '100',
        'sorting': 'random',
        'order': 'desc',
        'page': 1,
        'resolutions': '1920x1080'
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(site_url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    os.makedirs('downloaded_images', exist_ok=True)
    downloaded_files = []

    for image in data['data'][5]:
        img_url = image['path']
        if img_url:
            file_name = img_url.split('/')[-1]
            file_path = os.path.join('downloaded_images', file_name)
            img_data = requests.get(img_url).content

            with open(file_path, "wb") as file:
                file.write(img_data)
                downloaded_files.append(os.path.abspath(file_path))

    return downloaded_files

