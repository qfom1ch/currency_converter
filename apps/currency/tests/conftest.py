from unittest.mock import MagicMock

import pytest

from apps.currency.providers.base import CurrencyProvider
from apps.currency.service.service import CurrencyService


@pytest.fixture
def currency_provider_mock():
    return MagicMock(spec=CurrencyProvider)


@pytest.fixture
def currency_service(currency_provider_mock):
    return CurrencyService(currency_provider=currency_provider_mock)
