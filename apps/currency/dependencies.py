from apps.currency.providers.currate.currate import CurrateCurrencyProvider
from apps.currency.service.service import CurrencyService


async def get_currency_service_currate():
    return CurrencyService(CurrateCurrencyProvider())
