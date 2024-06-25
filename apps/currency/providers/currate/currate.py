from decimal import Decimal

import httpx
import pydantic
from httpx import codes

from apps.currency.providers.base import CurrencyProvider
from apps.currency.providers.schemas import CurrencyConversionResult
from config import CURRATE_TOKEN

from .schemas import CurrencyConversionResponse


class CurrateCurrencyProvider(CurrencyProvider):
    _currate_url = 'https://currate.ru/api/'

    async def currency_conversion(self, from_currency: str, to_currency: str) -> CurrencyConversionResult:
        currencies = f'{from_currency.upper()}{to_currency.upper()}'

        try:
            async with httpx.AsyncClient(base_url=self._currate_url) as client:
                r = await client.get(f'?get=rates&pairs={currencies}&key={CURRATE_TOKEN}')

            if r.status_code != codes.OK:
                return CurrencyConversionResult(success=False, detail='Http error')

            currate_conv_resp = CurrencyConversionResponse(**r.json())

            if currate_conv_resp.status != codes.OK:
                return CurrencyConversionResult(success=False, detail=currate_conv_resp.message)

            currency_value = currate_conv_resp.data.get(currencies)

            if not currency_value:
                return CurrencyConversionResult(success=False, detail='Http error')

        except httpx.HTTPError as e:
            return CurrencyConversionResult(success=False, detail=f'Http error: {e}')
        except pydantic.ValidationError as e:
            return CurrencyConversionResult(success=False, detail=f'Validation error: {e}')
        except Exception as e:
            return CurrencyConversionResult(success=False, detail=f'Unexpected error: {e}')

        return CurrencyConversionResult(success=True, value=Decimal(currency_value))
