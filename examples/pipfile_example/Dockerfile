FROM python:3.9.2-alpine

ARG development=no

# prevent python from creating __pycache__, and turn off output buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIPENV_DEV=${development}

WORKDIR /app

# First copy over the pipfile
# We aren't copying over the Pipfile.lock
# Because we need to install the application
# outside the container and we dont have a
# consistent python version there
# But if we were copying the pipfile.lock
# We'd install using --system and skip the venv creation
COPY Pipfile ./
RUN pip3 install -U pip && \
    pip3 install pipenv && \
    pipenv install

# Now copy application source over
COPY . .

CMD ["pipenv", "run", "python", "main.py"]
