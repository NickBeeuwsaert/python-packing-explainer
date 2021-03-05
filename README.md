# Overview of Python Packaging Formats

Python currently has several different ways to specify project dependencies, which kind of flies in the face of the Zen of Python. Fortunately, the situation is getting better. But even so, starting a new python project can be daunting and confusing.

## `requirements.txt`

The `requirements.txt` file is a text file with a list of arguments to pass to pip listed on each line.

Since it's a flat file, you are required to use multiple files for optional dependencies(`requirements-dev.txt`, `requirements-test.txt`, etc.), which can quickly become unmanageable.

This format is useful as a lockfile to create reproducible installs.

It can be unclear whether or not `requirements.txt` is supposed to be used to declare top-level dependencies, or every project dependency (e.g. as a lock file)

Uses:

- Smalls projects with simple dependency management needs
- Projects not meant to be published to a package index
- As package lockfiles for reproducible installs

## `Pipfile`

Designed to be a replacement to `requirements.txt`. This is a TOML-based format that lets you declare project dependencies.

The unclear distinction between using `requirements.txt` as a lock-file is solved, since tools using `Pipfile` will create a file named `Pipfile.lock`.

You can also specify dev dependencies, but not optional dependencies.

`Pipfile` does not allow you to specify project metadata such as a project name or other details. It is purely meant for dependencies.

Uses:

- Projects not meant to be installed or published to a package index

## `setup.py`

A Python script that calls a `distutils`-compatible library (Usually `setuptools`). You can specify dependencies (in `install_requires`) and also a list of "extras", which are optional dependencies.

Often you will see projects using `setup.py` and `requirements.txt` together. Although this is hacky, since requirements.txt is a list of pip options, and thus can have lines that don't translate into the `install_requires` (such as `--extra-index-url` or `--hash`)

Uses:

- For packages which need to be installed, like libraries or packages
- For projects which need to be published to a package index

## `setup.cfg`

Fulfills the same purpose of `setup.py`, but allows you to declare your project metadata and dependencies in a declarative fashion.

You can use `setup.cfg` without a `setup.py`, unless you want to do an editable install. If you need to do an editable install you will need a blank setup.py file:

```py
from setuptools import setup

setup()
```

Uses:

- Same as `setup.py`

## `pyproject.toml`

Originally introduced in [PEP 518](https://www.python.org/dev/peps/pep-0518/#file-format) to specify build requirements for a project, as well as tooling configuration, but as of [PEP 619](https://www.python.org/dev/peps/pep-0621/) has been extended to support project metadata as well.

Because PEP 518 specified a tools section, tools like [flit](https://flit.readthedocs.io/en/latest/index.html) or [poetry](https://python-poetry.org/) can store project metadata in this file.

Uses:

- To store requirements for the build system to function (not your actual code)
- For projects that need to be published or installed (for tools that support PEP 619, or if using tools like poetry)
- To store project metadata and dependencies (for tools that support PEP 619)
