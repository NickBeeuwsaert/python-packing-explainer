# Poetry example project

This example uses poetry (metadata stored in pyproject.toml) to specify a project

## Prerequisite Tools

| Tool              | Documentation                                                         |
| ----------------- | --------------------------------------------------------------------- |
| docker (Optional) | https://docs.docker.com/get-docker/                                   |
| pyenv             | https://github.com/pyenv/pyenv#simple-python-version-management-pyenv |
| poetry            | https://python-poetry.org/docs/#installation                          |

## Installation

| Docker                                            | Local            |
| ------------------------------------------------- | ---------------- |
| Make sure Docker and docker-compose are installed | `pyenv install`  |
|                                                   | `poetry install` |

## Running

If you use docker:

| Docker              | Local                                        |
| ------------------- | -------------------------------------------- |
| `docker-compose up` | `poetry run pserve development.ini --reload` |

## Testing

| Docker                                     | Local               |
| ------------------------------------------ | ------------------- |
| `docker-compose run web poetry run pytest` | `poetry run pytest` |
