Quickstart
==========

Overview
--------

ASGI RESTful API by `igorezersky/cookiecutter-api`_

Requirements
------------

Make sure that all requirements related for your platform will be
installed before main package installation.

Linux \| Windows \| macOS
~~~~~~~~~~~~~~~~~~~~~~~~~

Docker
~~~~~~

Normally, to build project image you will need to install following
packages:

-  `Python`_

-  `Docker`_ and `docker-compose`_

Installation
------------

.. _linux-windows-macos-1:

Linux \| Windows \| macOS
~~~~~~~~~~~~~~~~~~~~~~~~~

Following instructions are guidelines, you can install it differently,
however, executing the following commands will ensure that ``portfolio``
is installed correctly:

Clone repository and create `virtual environment`_:

.. code:: console

   foo@bar:~$ cd portfolio
   foo@bar:~/portfolio$ python -m venv venv && source venv/bin/activate
   foo@bar:~/portfolio$ python -m pip install --upgrade pip wheel setuptools

Install requirements:

.. code:: console

   foo@bar:~/portfolio$ pip install -r requirements/dev.txt

.. _docker-1:

Docker
~~~~~~

Make sure that you have execution permissions for ``docker``,
``docker-compose``, ``python`` and ``pydeployhelp``.

Use ``pydeployhelp`` package to build project image:

.. code:: console

   foo@bar:~/portfolio$ pydeployhelp
   Enter deploy tasks from following: all | build up down: build
           ✓ processing deploy tasks: build
   Enter deploy targets from following: all | portfolio-backend-dev: all
           ✓ processing deploy targets: portfolio-backend-dev
   Do you agree to start processing (y/N)?: y

Environment
-----------

Create ``.env`` file in project root with environment variables:

.. code:: text

   ENV=dev
   PROJECT_SLUG=portfolio
   HOST=localhost
   PORT=8080
   ENABLE_CORS=True
   VOLUMES_ROOT=$HOME/projects/portfolio

What does each variable mean:

-  ``ENV``: environment type (dev, prod), could contain any value, but
   for production please set ``ENV=prod``

-  ``PROJECT_SLUG``: this name will be used for docker containers
   creation

-  ``HOST``: backend host (e.g. localhost, project.dns.com)

-  ``PORT``: backend port, will be ignored when ``ENV=prod``

-  ``ENABLE_CORS``: if True, all origins and methods will be allowed

-  ``VOLUMES_ROOT``: path to directory, where docker volumes will be
   stored; it’s highly recommended to set this value to the path of the
   project root (on development machine) - this will allow you to use
   the same data when debugging from IDE and when deploying via docker
   (pydeployhelp)

Usage
-----

.. _linux-windows-macos-2:

Linux \| Windows \| macOS
~~~~~~~~~~~~~~~~~~~~~~~~~

You can manually start project:

.. code:: console

   foo@bar:~/portfolio$ python run.py

.. _docker-2:

Docker
~~~~~~

Use ``pydeployhelp`` package to run project image:

.. code:: console

   foo@bar:~/portfolio$ pydeployhelp
   Enter deploy tasks from following: all | build up down: up
           ✓ processing deploy tasks: up
   Enter deploy targets from following: all | portfolio-backend-dev: all
           ✓ processing deploy targets: portfolio-backend-dev
   Do you agree to start processing (y/N)?: y

.. _igorezersky/cookiecutter-api: https://github.com/igorezersky/cookiecutter-api
.. _Python: https://python.org/downloads
.. _Docker: https://docs.docker.com/get-docker/
.. _docker-compose: https://docs.docker.com/compose/install/
.. _virtual environment: https://docs.python.org/3/library/venv.html