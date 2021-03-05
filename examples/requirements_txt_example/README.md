# requirement.txt example project

This example uses a requirements.txt to specify a projects dependencies.

## Prerequisite Tools

| Tool              | Documentation                                                         |
| ----------------- | --------------------------------------------------------------------- |
| docker (Optional) | https://docs.docker.com/get-docker/                                   |
| pyenv             | https://github.com/pyenv/pyenv#simple-python-version-management-pyenv |

## Installation

| Docker                                            | Local                                                                 |
| ------------------------------------------------- | --------------------------------------------------------------------- |
| Make sure Docker and docker-compose are installed | `pyenv install`                                                       |
|                                                   | `python3 -m venv venv`                                                |
|                                                   | `./venv/bin/pip install -r requirements.txt -r requirements-test.txt` |

## Running

If you use docker:

| Docker              | Local                       |
| ------------------- | --------------------------- |
| `docker-compose up` | `./venv/bin/python main.py` |

## Testing

| Docker                          | Local                         |
| ------------------------------- | ----------------------------- |
| `docker-compose run web pytest` | `./venv/bin/python -m pytest` |
