from abc import ABC, abstractmethod

from apps.currency.providers.schemas import CurrencyConversionResult


class CurrencyProvider(ABC):
    @abstractmethod
    async def currency_conversion(self, from_currency: str, to_currency: str) -> CurrencyConversionResult:
        ...
