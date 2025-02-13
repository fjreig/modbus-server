
from datetime import datetime
from pydantic import BaseModel

class NecesidadesRequest(BaseModel):
    date_at: str
    bomba: int
    horas_max: int
    horas_min: int

    class Config:
        json_schema_extra = {
            "example": {
                'date_at' : "2025-01-01 00:00:00",
                'bomba' : 1,
                'horas_max': 4,
                'horas_min': 2
            }
        }

class PrecioRequest(BaseModel):
    date_at: str

    class Config:
        json_schema_extra = {
            "example": {
                'date_at' : "2025-01-01",
            }
        }