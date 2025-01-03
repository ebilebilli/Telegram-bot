from aiogram.types import FSInputFile
from aiogram import types
from request_system import download_images
import os

async def send_category_images(message: types.Message, category_url):
    await message.answer('Downloading images....')
    downloaded_files = download_images(category_url, num_images=10)
    
    if not downloaded_files:
        await message.answer('We could not find images for your request')
        return

    for file_path in downloaded_files:
        full_path = os.path.abspath(file_path)

        await message.answer_document(FSInputFile(full_path))
        
     