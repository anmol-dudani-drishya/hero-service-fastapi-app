import uvicorn
from fastapi import FastAPI, HTTPException
from src.app import app
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
