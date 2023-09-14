import os

from dotenv import load_dotenv

load_dotenv('.env.example')

CURRENCY_TOKEN = os.environ.get('CURRENCY_TOKEN')
