FROM python:3.12

RUN apt-get update --fix-missing && apt-get install -y --no-install-recommends \
    aptitude bash curl libffi-dev libpq5 libssl-dev openssl libjpeg62 zlib1g webp libgmp-dev && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 - --version 1.8.3 && \
    poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . /app

RUN chmod +x /app/start.sh

ENTRYPOINT ["/app/start.sh"]
