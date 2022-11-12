# Jump 2 Digital - Backend

Proyecto de challenge de Backend para Jump 2 Digital.

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=IanStory99_jump2digital-backend&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=IanStory99_jump2digital-backend)
[![CodeFactor](https://www.codefactor.io/repository/github/ianstory99/jump2digital-backend/badge/main)](https://www.codefactor.io/repository/github/ianstory99/jump2digital-backend/overview/main)

## Descripción
Este proyecto tiene como objetivo disponibilizar Endpoints para obtener información sobre diversas compañías, ya sea de forma ordenada o usando agregaciones.

## API

Operaciones disponibles
```
GET /company?order=<founded|size> -> Obtiene todas las compañías ordenadas por tamaño o fecha de fundación.
GET /company/summary -> Obtiene un resumen de las compañías, agrupando la cantidad de industrias, tamaño y año fundado.
```

## Instalación

Sin Docker
```shell
    # Requiere Python 3.10.5
    python -m venv j2d-venv
    source j2d-venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    # http://localhost:5000/docs para Swagger

    # Para correr las pruebas
    python manage.py test
```

Con Docker
```shell
    docker compose up
    # http://localhost:5000/docs para Swagger
```
