# Portfolio

## Overview

ASGI RESTful API by [igorezersky/cookiecutter-api](https://github.com/igorezersky/cookiecutter-api)

## Requirements

Make sure that all requirements related for your platform will be installed before main package installation.

### Linux | Windows | macOS

### Docker

Normally, to build project image you will need to install following packages:

- [Python](https://python.org/downloads)

- [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/)

## Installation

### Linux | Windows | macOS

Following instructions are guidelines, you can install it differently, however,
executing the following commands will ensure that `portfolio` is installed correctly:

Clone repository and create [virtual environment](https://docs.python.org/3/library/venv.html):

```console
foo@bar:~$ cd portfolio
foo@bar:~/portfolio$ python -m venv venv && source venv/bin/activate
foo@bar:~/portfolio$ python -m pip install --upgrade pip wheel setuptools
```

Install requirements:

```console
foo@bar:~/portfolio$ pip install -r requirements/dev.txt
```

### Docker

Make sure that you have execution permissions for `docker`, `docker-compose`, `python` and `pydeployhelp`.

Use `pydeployhelp` package to build project image:

```console
foo@bar:~/portfolio$ pydeployhelp
Enter deploy tasks from following: all | build up down: build
        ✓ processing deploy tasks: build
Enter deploy targets from following: all | portfolio-db portfolio-backend: all
        ✓ processing deploy targets: portfolio-db portfolio-backend
Do you agree to start processing (yes or no)? [yes]: yes
```

## Environment

Create `.env` file in project root with environment variables:

```text
ENV=dev
PROJECT_SLUG=portfolio
HOST=localhost
PORT=8080
ENABLE_CORS=True
VOLUMES_ROOT=$HOME/projects/portfolio
```

What does each variable mean:

* `ENV`: environment type (dev, prod), could contain any value, but for production please set `ENV=prod`

* `PROJECT_SLUG`: this name will be used for docker containers creation

* `HOST`: backend host (e.g. localhost, project.dns.com)

* `PORT`: backend port, will be ignored when `ENV=prod`

* `ENABLE_CORS`: if True, all origins and methods will be allowed

* `VOLUMES_ROOT`: path to directory, where docker volumes will be stored; it's highly recommended to set this value to the path of the project root (on development machine) - this will allow you to use the same data when debugging from IDE and when deploying via docker (pydeployhelp)

## Usage

### Linux | Windows | macOS

You can manually start project:

```console
foo@bar:~/portfolio$ python run.py
```

### Docker

Use `pydeployhelp` package to run project image:

```console
foo@bar:~/portfolio$ pydeployhelp
Enter deploy tasks from following: all | build up down: up
        ✓ processing deploy tasks: up
Enter deploy targets from following: all | portfolio-db portfolio-backend: all
        ✓ processing deploy targets: portfolio-db portfolio-backend
Do you agree to start processing (yes or no)? [yes]: yes
```
