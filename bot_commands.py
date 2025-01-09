from aiogram import Bot, Dispatcher
from aiogram.types import Message, BotCommand
from aiogram.filters import Command
from sending_system import send_images
import settings
import asyncio

bot = Bot(token=settings.TOKEN)
dp = Dispatcher()

async def command_list():
    commands = [
        BotCommand(command='/info', description='Information about the bot'),
        BotCommand(command='/search', description='Use /search "category name" to get the image'),
    ]
    await bot.set_my_commands(commands)


@dp.message(Command('info'))
async def cmd_info(message: Message):
    await message.answer(settings.INFO_MESSAGE)

@dp.message(Command('search'))
async def cmd_search(message: Message):

    await send_images(message)

    
  