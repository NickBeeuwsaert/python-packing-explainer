# Setuptools example project

This example uses setuptools (setup.py + setup.cfg + pyproject.toml) to specify a project with dependencies.

We are using setup.cfg for all metadata, and setup.py just for editable installs, but it is easy enough to convert the project into just using setup.py

## Prerequisite Tools

| Tool              | Documentation                                                         |
| ----------------- | --------------------------------------------------------------------- |
| docker (Optional) | https://docs.docker.com/get-docker/                                   |
| pyenv             | https://github.com/pyenv/pyenv#simple-python-version-management-pyenv |

## Installation

| Docker                                            | Local                               |
| ------------------------------------------------- | ----------------------------------- |
| Make sure Docker and docker-compose are installed | `pyenv install`                     |
|                                                   | `python3 -m venv venv`              |
|                                                   | `./venv/bin/pip install -e.[tests]` |

## Running

If you use docker:

| Docker              | Local                                        |
| ------------------- | -------------------------------------------- |
| `docker-compose up` | `./venv/bin/pserve development.ini --reload` |

## Testing

| Docker                          | Local               |
| ------------------------------- | ------------------- |
| `docker-compose run web pytest` | `./venv/bin/pytest` |
