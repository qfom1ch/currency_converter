from fastapi import APIRouter, Depends, HTTPException, Query, status

from apps.currency.dependencies import get_currency_service_currate
from apps.currency.routers.schemas import ShowCurrency
from apps.currency.service.schemas import GetCurrencyConversionRes
from apps.currency.service.service import CurrencyService

currency_router = APIRouter(
    prefix='/api'
)


@currency_router.get("/rates", response_model=ShowCurrency, tags=['currency'])
async def get_currency_conversion(from_currency: str = Query(..., min_length=3, max_length=3),
                                  to_currency: str = Query(..., min_length=3, max_length=3),
                                  quantity: int = Query(1, gt=0),
                                  currency_service: CurrencyService = Depends(get_currency_service_currate),
                                  ) -> ShowCurrency:
    result: GetCurrencyConversionRes = await currency_service.get_currency_conversion(
        from_currency=from_currency, to_currency=to_currency, quantity=quantity,
    )

    if not result.success:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f'Service unavailable please try later. Error: {result.detail}',
        )

    return ShowCurrency(result=result.value)
