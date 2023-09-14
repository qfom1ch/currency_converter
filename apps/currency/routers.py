from fastapi import APIRouter, HTTPException, status

from apps.currency.schemas import ShowCurrency
from apps.currency.services import _get_currency

currency_router = APIRouter(
    prefix='/api'
)


@currency_router.get("/rates", response_model=ShowCurrency, tags=['currency'])
async def get_currency(from_currency: str, to_currency: str,
                       value: int = 1) -> ShowCurrency:
    if len(from_currency) != 3 or len(to_currency) != 3:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The name of the currency must consist of three letters.",
        )

    if value <= 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Value cannot be 0 or less.",
        )

    currencies = from_currency.upper() + to_currency.upper()
    currency_rate = await _get_currency(currencies)
    result = currency_rate * value
    return {
        'result': result
    }
