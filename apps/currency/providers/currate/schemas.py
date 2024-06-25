from pydantic import BaseModel


class CurrencyConversionResponse(BaseModel):
    status: int
    message: str
    data: dict[str, str]
