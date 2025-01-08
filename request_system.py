import requests
from bs4 import BeautifulSoup
import os

def download_images(category_url, num_images=1):
    headers = {
    "User-Agent": "Mozilla/5.0 ...",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8"
}
    try:
        response = requests.get(category_url, headers=headers)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return []  

    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')[:num_images]  

    os.makedirs('downloaded_images', exist_ok=True)  
    downloaded_files = []
    for img in images:
        img_url = img.get('src')
        if img_url:
            file_name = img_url.split("/")[-1]
            file_path = os.path.join('downloaded_images', file_name)
            try:
                img_data = requests.get(img_url).content
                with open(file_path, "wb") as file:
                    file.write(img_data)
                downloaded_files.append(os.path.abspath(file_path))
            except Exception as e:
                print(f'Error downloading {img_url}: {e}')

    return downloaded_files if downloaded_files else None
