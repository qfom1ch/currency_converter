from decimal import Decimal

from pydantic import BaseModel


class CurrencyConversionResult(BaseModel):
    success: bool
    detail: str | None = None
    value: Decimal | None = None
