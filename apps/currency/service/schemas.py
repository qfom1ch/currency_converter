from decimal import Decimal

from pydantic import BaseModel


class GetCurrencyConversionRes(BaseModel):
    success: bool
    detail: str | None = None
    value: Decimal | None = None
