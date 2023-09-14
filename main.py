import uvicorn
from fastapi import FastAPI

from apps.currency.routers import currency_router

app = FastAPI(title='test_app')

app.include_router(currency_router)

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
