from apps.currency.providers.base import CurrencyProvider
from apps.currency.providers.currate.currate import CurrateCurrencyProvider
from apps.currency.providers.schemas import CurrencyConversionResult

from .schemas import GetCurrencyConversionRes


class CurrencyService:
    def __init__(self, currency_provider: CurrencyProvider):
        self._currency_provider = currency_provider

    async def get_currency_conversion(self, from_currency: str, to_currency: str, quantity: int)\
            -> GetCurrencyConversionRes:

        res: CurrencyConversionResult = \
            await self._currency_provider.currency_conversion(from_currency=from_currency, to_currency=to_currency)

        if not res.success:
            return GetCurrencyConversionRes(success=False, detail=res.detail)

        return GetCurrencyConversionRes(success=True, value=res.value * quantity)


def get_currency_service_currate():
    return CurrencyService(CurrateCurrencyProvider())
