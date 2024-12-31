import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from request_system import download_images
from aiogram.types import InputFile


import urls
from messages_to_user import starting_message, info_message

async def command_list():
    commands = [
        BotCommand(command="/start", description='Start the bot'),
        BotCommand(command='/info', description='Information about the bot'),
        BotCommand(command='/abstract', description='Abstract category'),
        BotCommand(command='/anime', description='Anime category'),
        BotCommand(command='/artist', description='Artist category'),
        BotCommand(command='/bikes', description='Bikes category'),
        BotCommand(command='/cars', description='Cars category'),
        BotCommand(command='/celebrities', description='Celebrities category'),
        BotCommand(command='/computer', description='Computer category'),
        BotCommand(command='/fantasy_girls', description='Fantasy Girls category'),
        BotCommand(command='/games', description='Games category'),
        BotCommand(command='/girls', description='Girls category'),
        BotCommand(command='/love', description='Love category'),
        BotCommand(command='/movies', description='Movies category'),
        BotCommand(command='/music', description='Music category'),
        BotCommand(command='/nature', description='Nature category'),
        BotCommand(command='/photography', description='Photography category'),
        BotCommand(command='/superheroes', description='Superheroes category'),
        BotCommand(command='/tv_shows', description='TV Shows category'),
        BotCommand(command='/universe', description='Universe category'),
        BotCommand(command='/world', description='World category'),
    ]
    await bot.set_my_commands(commands)



bot = Bot(token=urls.TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(starting_message)

@dp.message(Command('info'))
async def cmd_talk(message: Message):
    await message.answer(info_message)
@dp.message(Command('abstract'))
async def cmd_abstract(message: Message):
    category_url = urls.Abstract
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)
        await message.answer_document(open(file_path, "rb"))

# Superheroes category
@dp.message(Command('superheroes'))
async def cmd_superheroes(message: Message):
    category_url = urls.Superheroes
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Games category
@dp.message(Command('games'))
async def cmd_games(message: Message):
    category_url = urls.Games
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Artist category
@dp.message(Command('artist'))
async def cmd_artist(message: Message):
    category_url = urls.Artist
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Movies category
@dp.message(Command('movies'))
async def cmd_movies(message: Message):
    category_url = urls.Movies
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Celebrities category
@dp.message(Command('celebrities'))
async def cmd_celebrities(message: Message):
    category_url = urls.Celebrities
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Cars category
@dp.message(Command('cars'))
async def cmd_cars(message: Message):
    category_url = urls.Cars
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Nature category
@dp.message(Command('nature'))
async def cmd_nature(message: Message):
    category_url = urls.Nature
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Girls category
@dp.message(Command('girls'))
async def cmd_girls(message: Message):
    category_url = urls.Girls
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# TV Shows category
@dp.message(Command('tv_shows'))
async def cmd_tv_shows(message: Message):
    category_url = urls.TV_Shows
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Anime category
@dp.message(Command('anime'))
async def cmd_anime(message: Message):
    category_url = urls.Anime
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)
# Music category
@dp.message(Command('music'))
async def cmd_music(message: Message):
    category_url = urls.Music
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Photography category
@dp.message(Command('photography'))
async def cmd_photography(message: Message):
    category_url = urls.Photography
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Computer category
@dp.message(Command('computer'))
async def cmd_computer(message: Message):
    category_url = urls.Computer
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Animals category
@dp.message(Command('animals'))
async def cmd_animals(message: Message):
    category_url = urls.Animals
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Universe category
@dp.message(Command('universe'))
async def cmd_universe(message: Message):
    category_url = urls.Universe
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# World category
@dp.message(Command('world'))
async def cmd_world(message: Message):
    category_url = urls.World
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Bikes category
@dp.message(Command('bikes'))
async def cmd_bikes(message: Message):
    category_url = urls.Bikes
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Fantasy Girls category
@dp.message(Command('fantasy_girls'))
async def cmd_fantasy_girls(message: Message):
    category_url = urls.Fantasy_Girls
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)

# Love category
@dp.message(Command('love'))
async def cmd_love(message: Message):
    category_url = urls.Love
    await message.answer("Images downloading...")
    downloaded_files = download_images(category_url, num_images=10)

    for file_path in downloaded_files:
        input_file = InputFile(file_path)  
        await message.answer_document(input_file)