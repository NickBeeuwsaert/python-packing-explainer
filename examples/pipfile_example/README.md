# Pipefile example project

This example uses Pipfile to specify a projects dependencies.

## Prerequisite Tools

| Tool              | Documentation                                                         |
| ----------------- | --------------------------------------------------------------------- |
| docker (Optional) | https://docs.docker.com/get-docker/                                   |
| pyenv             | https://github.com/pyenv/pyenv#simple-python-version-management-pyenv |
| pipenv            | https://pipenv.pypa.io/en/latest/install/#installing-pipenv           |

## Installation

| Docker                                            | Local            |
| ------------------------------------------------- | ---------------- |
| Make sure Docker and docker-compose are installed | `pyenv install`  |
|                                                   | `pipenv install` |

## Running

If you use docker:

| Docker              | Local                       |
| ------------------- | --------------------------- |
| `docker-compose up` | `pipenv run python main.py` |

## Testing

| Docker                                               | Local                         |
| ---------------------------------------------------- | ----------------------------- |
| `docker-compose run web pipenv run python -m pytest` | `pipenv run python -m pytest` |
