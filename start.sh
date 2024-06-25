#! /bin/bash

echo "Start currency converter"

exec gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
