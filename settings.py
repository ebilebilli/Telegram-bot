from dotenv import load_dotenv
import os
load_dotenv('.gitignore/.env')

INFO_MESSAGE = os.getenv('info_message')

TOKEN = os.getenv('Token')
SITE_URL = os.getenv('Site_Url')
API_KEY = os.getenv('Api_Key')

