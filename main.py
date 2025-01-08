import asyncio
from bot_commands import command_list, dp, bot

async def main():
    await command_list()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main()) 







