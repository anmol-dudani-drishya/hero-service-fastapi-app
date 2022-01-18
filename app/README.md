# Hero Service FastAPI app

This application is developed to demonstrate the possibilities and capabilities of [FastAPI](https://fastapi.tiangolo.com/)

## Awesome things I came to know by developing this application

- Swagger UI - An Interactive REST API IDE is available by default.
- ReDoc - OpenAPI Standard Docs for the apis - This integration is also available by  dfault.
- The Documentation of [fastAPI](https://fastapi.tiangolo.com/) is very good
- [Pydantic - Data validation and settings management using python type annotations](https://pydantic-docs.helpmanual.io/)

## Use Case

Many Super heros are available to help. There are plenty of assignments the heros can help with. We need an application to manage the heros time so that we can leverage their capabilities to wrap up most of the assignments.

## Development

### Prerequisites

- Python 3.6+
- [Table Plus](https://tableplus.com/)
  - This is useful while developing and playing with Database

### Folder Structure

```text
src/                        Source Code
----models/                 Models/Schemas for SQL Alchemy
----schemas/                Models/Schemas powered by Pedantic. These used for validation.
----routers/                Routes for entities/tables
----repositories/           DataBase operations
----app.py                  App entry
----database.py             Database Connection
```

### Start the app in development mode

Clone this repository

```bash
git clone https://github.com/sravanrekandar/hero-service-fastapi-app.git && cd hero-service-fastapi-app
```

Set permissions to execute start.sh. This is required only one time.

```bash
chmod 777 start.sh
```

```bash
./start.sh
```

- App will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger UI - An Interactive REST API IDE [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- OpenAPI Docs [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
