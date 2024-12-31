import asyncio
from cmd_func_list import command_list, dp, bot


async def main():
    await command_list()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())







