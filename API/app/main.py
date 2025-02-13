import uvicorn
from fastapi import FastAPI, Depends

from app.routes import router as ruta

tags_metadata = [
    {
        "name": "modbus",
        "description": "modbus_server",
    }
]

app = FastAPI()

app.include_router(ruta, tags=["modbus"], prefix="/modbus")