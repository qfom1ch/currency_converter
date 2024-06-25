from decimal import Decimal

from pydantic import BaseModel


class ShowCurrency(BaseModel):
    result: Decimal
