from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.monitoring import logging_config
from app.middlewares.correlation_id_middleware import CorrelationIdMiddleware
from app.middlewares.logging_middleware import LoggingMiddleware
from app.handlers.exception_handler import exception_handler
from app.handlers.http_exception_handler import http_exception_handler
import uuid
import uvicorn
from mangum import Mangum


app = FastAPI()

logging_config.configure_logging(
    level="DEBUG", service="Helloworld", instance=str(uuid.uuid4())
)

app.add_exception_handler(Exception, exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

app.add_middleware(LoggingMiddleware)
app.add_middleware(CorrelationIdMiddleware)


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/id/{id}")
async def test(id: int):
    return "Hello User " + str(id)


@app.get("/test")
async def test1():
    return "Hello World"


@app.post("/items/")
async def create_item(item: Item):
    return item


# Handler for AWS Lambda
handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
