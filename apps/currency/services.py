from decimal import Decimal

import httpx

from config import CURRENCY_TOKEN


async def _get_currency(currencies):
    url = (f'https://currate.ru/api/?get=rates&pairs={currencies}&key='
           f'{CURRENCY_TOKEN}')
    async with httpx.AsyncClient() as client:
        request = await client.get(url)
    currency_value = list(request.json()['data'].values())[0]
    return Decimal(currency_value)
