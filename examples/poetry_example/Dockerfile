FROM python:3.9.2-alpine

ARG extras

# prevent python from creating __pycache__, and turn off output buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.1.4 \
    PATH="${HOME}/.poetry/bin:${PATH}"

WORKDIR /app

COPY pyproject.toml ./
RUN apk add \
    --no-cache --virtual .build-deps \
    gcc musl-dev python3-dev libffi-dev openssl-dev cargo && \
    pip install -U pip && \
    pip install --no-binary=cryptography poetry==${POETRY_VERSION} && \
    apk del .build-deps && \
    # Have poetry install things globally
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root --no-dev ${extras:+-E "${extras}"}

COPY src src
# Install the rest of the dependencies (the root app)
# this installs in editable mode
RUN poetry install --no-interaction --no-ansi


