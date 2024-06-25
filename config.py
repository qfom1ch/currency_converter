import os

from dotenv import load_dotenv

load_dotenv('.env.example')

CURRATE_TOKEN = os.environ.get('CURRENCY_TOKEN')
