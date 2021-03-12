# Hero Service FastAPI app

## Folder Structure

```text
src/                        Source Code
----models/                 Models/Schemas for SQL Alchemy
----schemas/                Models/Schemas powered by Pedantic. These used for validation.
----routers/                Routes for entities/tables
----repositories/           DataBase operations
----app.py                  App entry
----database.py             Database Connection
```

## Start the app in development mode

To set permissions to execute. This is required only one time.

```bash
chmod 777 start.sh
```

```bash
./start.sh
```

Then you navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
