from pydantic import BaseModel


class ShowCurrency(BaseModel):
    result: float
