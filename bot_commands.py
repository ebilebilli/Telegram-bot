from aiogram import Bot, Dispatcher
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from sending_system import send_category_images
import settings

bot = Bot(token=settings.TOKEN)
dp = Dispatcher()

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


@dp.message(Command('info'))
async def cmd_info(message: Message):
    await message.answer(settings.INFO_MESSAGE)


@dp.message(Command('abstract'))
async def cmd_artist(message: Message):
    await send_category_images(message, settings.ABSTRACT)

@dp.message(Command('anime'))
async def cmd_artist(message: Message):
    await send_category_images(message, settings.ANIME)

@dp.message(Command('artist'))
async def cmd_artist(message: Message):
    await send_category_images(message, settings.ARTIST)

@dp.message(Command('bikes'))
async def cmd_bikes(message: Message):
    await send_category_images(message, settings.BIKES)

@dp.message(Command('cars'))
async def cmd_cars(message: Message):
    await send_category_images(message, settings.CARS)

@dp.message(Command('celebrities'))
async def cmd_celebrities(message: Message):
    await send_category_images(message, settings.CELEBRITIES)

@dp.message(Command('computer'))
async def cmd_computer(message: Message):
    await send_category_images(message, settings.COMPUTER)

@dp.message(Command('fantasy_girls'))
async def cmd_fantasy_girls(message: Message):
    await send_category_images(message, settings.FANTASY_GIRLS)

@dp.message(Command('games'))
async def cmd_games(message: Message):
    await send_category_images(message, settings.GAMES)

@dp.message(Command('girls'))
async def cmd_girls(message: Message):
    await send_category_images(message, settings.GIRLS)

@dp.message(Command('love'))
async def cmd_love(message: Message):
    await send_category_images(message, settings.LOVE)

@dp.message(Command('movies'))
async def cmd_movies(message: Message):
    await send_category_images(message, settings.MOVIES)

@dp.message(Command('music'))
async def cmd_music(message: Message):
    await send_category_images(message, settings.MUSIC)

@dp.message(Command('nature'))
async def cmd_nature(message: Message):
    await send_category_images(message, settings.NATURE)

@dp.message(Command('photography'))
async def cmd_photography(message: Message):
    await send_category_images(message, settings.PHOTOGRAPHY)

@dp.message(Command('superheroes'))
async def cmd_superheroes(message: Message):
    await send_category_images(message, settings.SUPERHEROES)

@dp.message(Command('tv_shows'))
async def cmd_tv_shows(message: Message):
    await send_category_images(message, settings.TV_SHOWS)

@dp.message(Command('universe'))
async def cmd_universe(message: Message):
    await send_category_images(message, settings.UNIVERSE)

@dp.message(Command('world'))
async def cmd_world(message: Message):
    await send_category_images(message, settings.WORLD)
