from aiogram.types import FSInputFile
from aiogram import types
from request_system import request_system
import os

async def send_images(message: types.Message):
    await message.answer('Downloading images....')

    category_name = message.text.split(maxsplit=1)[1].strip().lower()   
    downloaded_files = request_system(category_name=category_name, num_images=1)

    for file_path in downloaded_files:
        full_path = os.path.abspath(file_path)
        
        await message.answer_document(FSInputFile(full_path))