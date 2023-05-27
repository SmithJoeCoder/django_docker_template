# Run Django with Docker Compose

This repo is for boilerplate of Django project with Docker Compose.

Just for faster deployment and skip the boring part of starting a django project.

This repo will create 3 containers. such as:

- django
- postgres
- redis

It includes the following:

-   `poetry` for dependency management
-   `ruff`, `black` for linting / format
-   `pre-commit` to run linting
-   `mypy` for type checking
-   `django-postgres-extra` for django postgres partition tables.
-   `celery` for distributed task queue

