from fastapi import FastAPI, Depends, APIRouter

from app.modbus import(
    leer_modbus_unit,
    escribir_modbus_unit,
    leer_modbus_int16,
    leer_modbus_int32,
    escribir_modbus_int16,
    escribir_modbus_int32
)

router = APIRouter()

@router.get("/Read/uint/{registro}/{esclavo}", summary="read holding register")
async def read_notification_id(registro: int, esclavo: int):
    value = leer_modbus_unit(registro, 1, esclavo)
    return (value)

@router.post("/Write/uint/{registro}/{valor}/{esclavo}", summary="write holding register")
async def create_notification(registro: int, valor: int, esclavo: int):
    value = escribir_modbus_unit(registro, valor, esclavo)
    return (value)

@router.get("/Read/int/{registro}/{esclavo}", summary="read holding register")
async def read_notification_id(registro: int, esclavo: int):
    value = leer_modbus_int16(registro, 2, esclavo)
    return (value)

@router.post("/Write/int/{registro}/{valor}/{esclavo}", summary="write holding register")
async def create_notification(registro: int, valor: int, esclavo: int):
    value = escribir_modbus_int16(registro, valor, esclavo)
    return (value)

@router.get("/Read/int32/{registro}/{esclavo}", summary="read holding register")
async def read_notification_id(registro: int, esclavo: int):
    value = leer_modbus_int32(registro, 4, esclavo)
    return (value)

@router.post("/Write/int32/{registro}/{valor}/{esclavo}", summary="write holding register")
async def create_notification(registro: int, valor: int, esclavo: int):
    value = escribir_modbus_int32(registro, valor, esclavo)
    return (value)