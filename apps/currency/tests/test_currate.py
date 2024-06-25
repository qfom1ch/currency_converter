from unittest.mock import AsyncMock

import pytest

from apps.currency.providers.schemas import CurrencyConversionResult


@pytest.mark.asyncio
async def test_get_currency_conversion_success(currency_service, currency_provider_mock):
    currency_provider_mock.currency_conversion = AsyncMock(
        return_value=CurrencyConversionResult(success=True, value=92)
    )

    res = await currency_service.get_currency_conversion('RUB', 'USD', 1)

    assert res.success
    assert res.value == 92
    currency_provider_mock.currency_conversion.assert_called_once_with(from_currency='RUB', to_currency='USD')


@pytest.mark.asyncio
async def test_get_currency_conversion_failure(currency_service, currency_provider_mock):
    currency_provider_mock.currency_conversion = AsyncMock(
        return_value=CurrencyConversionResult(success=False, detail="Error")
    )

    res = await currency_service.get_currency_conversion('ERR', 'USD', 10)

    assert not res.success
    assert res.detail
    currency_provider_mock.currency_conversion.assert_called_once_with(from_currency='ERR', to_currency='USD')
