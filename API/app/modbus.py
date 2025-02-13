import pymodbus.client as ModbusClient
from pymodbus import  FramerType, ModbusException, pymodbus_apply_logging_config
import os
import struct

from app.conversiones import(
    int_to_uint,
    uint_to_int,
    int16_to_two_uint8,
    two_uint8_to_int16,
    int32_to_four_uint8,
    four_uint8_to_int32
)

MODBUS_SERVER_HOST: str = os.environ['host']
MODBUS_SERVER_PORT: str = os.environ['port']

client: ModbusClient.ModbusBaseSyncClient
client = ModbusClient.ModbusTcpClient(
    MODBUS_SERVER_HOST,
    port=MODBUS_SERVER_PORT,
    framer=FramerType.SOCKET,
)
client.connect()

### UINT
def leer_modbus_unit(registro, num_reg, esclavo):
    try:
        rr = client.read_holding_registers(registro, count=num_reg, slave=esclavo)
    except ModbusException as exc:
        return({'Error': f"Received ModbusException({exc}) from library"})
    if rr.isError():
        return({'Error': f"Received exception from device ({rr})"})
    value = client.convert_from_registers(rr.registers, data_type=client.DATATYPE.INT16)
    return({'registro': registro, 'valor': value})

def escribir_modbus_unit(registro, valor, esclavo):
    valor = int_to_uint(valor)
    try:
        rr = client.write_register(registro, value=valor, slave=esclavo)
    except ModbusException as exc:
        return({'Error': f"Received ModbusException({exc}) from library"})
    if rr.isError():
        return({'Error': f"Received exception from device ({rr})"})
    value = client.convert_from_registers(rr.registers, data_type=client.DATATYPE.INT16)
    return({'registro': registro, 'valor': value})

### INT16
def leer_modbus_int16(registro, num_reg, esclavo):
    try:
        rr = client.read_holding_registers(registro, count=num_reg, slave=esclavo)
    except ModbusException as exc:
        return({'Error': f"Received ModbusException({exc}) from library"})
    if rr.isError():
        return({'Error': f"Received exception from device ({rr})"})
    value = client.convert_from_registers(rr.registers, data_type=client.DATATYPE.INT16)
    value2 = two_uint8_to_int16(value[0], value[1])
    return({'registro': registro, 'valor': value, 'valor2': value2})

def escribir_modbus_int16(registro, valor, esclavo):
    (valor1, valor2) = int16_to_two_uint8(valor)
    try:
        rr = client.write_registers(registro, values=[valor1, valor2], slave=esclavo)
    except ModbusException as exc:
        return({'Error': f"Received ModbusException({exc}) from library"})
    if rr.isError():
        return({'Error': f"Received exception from device ({rr})"})
    value = client.convert_from_registers(rr.registers, data_type=client.DATATYPE.INT16)
    return({'registro': registro, 'valor': value})

### INT32
def leer_modbus_int32(registro, num_reg, esclavo):
    try:
        rr = client.read_holding_registers(registro, count=num_reg, slave=esclavo)
    except ModbusException as exc:
        return({'Error': f"Received ModbusException({exc}) from library"})
    if rr.isError():
        return({'Error': f"Received exception from device ({rr})"})
    value = client.convert_from_registers(rr.registers, data_type=client.DATATYPE.INT16)
    value2 = four_uint8_to_int32(value[0], value[1], value[2], value[3])
    return({'registro': registro, 'valor': value, 'valor2': value2})

def escribir_modbus_int32(registro, valor, esclavo):
    (valor1, valor2, valor3, valor4) = int32_to_four_uint8(valor)
    try:
        rr = client.write_registers(registro, values=[valor1, valor2, valor3, valor4], slave=esclavo)
    except ModbusException as exc:
        return({'Error': f"Received ModbusException({exc}) from library"})
    if rr.isError():
        return({'Error': f"Received exception from device ({rr})"})
    value = client.convert_from_registers(rr.registers, data_type=client.DATATYPE.INT32)
    return({'registro': registro, 'valor': value})