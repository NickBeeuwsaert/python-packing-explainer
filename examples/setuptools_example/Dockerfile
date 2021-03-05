FROM python:3.9.2-alpine

ARG editable
ARG extras

# prevent python from creating __pycache__, and turn off output buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY setup.py setup.cfg pyproject.toml ./
RUN pip install -U pip && \
    # Create an empty src directory to trick pip into installing
    # just the dependencies
    mkdir src && \
    # Install the dependencies + any extras
    pip install .${extras:+[${extras}]}

COPY src src
# Now install the application for real, skipping the dependencies, since they are
# already installed
RUN pip install --no-deps ${editable:+-e}.

# No CMD specified, that will be specified in docker-compose
