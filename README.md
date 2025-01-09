Telegram Wallpaper Bot
Overview
This project is a Telegram bot designed to provide users with wallpapers based on their search criteria using the aiogram library for Telegram Bot API.

Project Structure
main.py: Contains the main logic for bot initialization, command handling, and image sending.
sending_system.py: Manages the downloading and processing of images.
request_system.py: Handles the API requests to fetch image data.
settings.py: Stores configuration variables like bot token and API keys.

Dependencies
aiogram: For Telegram bot functionality.
requests: To make HTTP requests for image downloads.
os: For file operations.

Installation
Clone the repository:
bash
git clone [your-repository-url]
Install dependencies:
bash
pip install aiogram requests
Configuration:
Create a settings.py file with the following content:
python
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
API_KEY = 'YOUR_API_KEY'
SITE_URL = 'URL_OF_THE_API_SERVICE'
INFO_MESSAGE = 'Welcome to Wallpaper Bot! Use /search "category" to find wallpapers.'

Usage
Run the bot:
bash
python main.py
Available commands:
/info: Displays information about the bot.
/search "category name": Search for wallpapers in the specified category.

Code Overview
Bot Initialization
python
bot = Bot(token=settings.TOKEN)
dp = Dispatcher()

Command Setup
python
async def command_list():
    commands = [
        BotCommand(command='/info', description='Information about the bot'),
        BotCommand(command='/search', description='Use /search "category name" to get the image'),
    ]
    await bot.set_my_commands(commands)

Command Handlers
/info: Sends a predefined message from settings.
/search: Triggers image fetching and sending.

Image Handling
request_system.py uses the requests library to fetch image data from an API.
sending_system.py processes and sends the downloaded images back to the user.

Note
The bot downloads images to a local directory downloaded_images. Ensure you have enough disk space and adjust permissions if necessary.
Ensure the API_KEY and SITE_URL are correctly set in settings.py for the bot to function properly.