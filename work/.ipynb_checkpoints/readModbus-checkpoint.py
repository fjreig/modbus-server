from pymodbus.client import ModbusTcpClient

host = "modbus-server"
port = 5020

cliente = ModbusTcpClient(host, port)
reg1 = cliente.read_holding_registers(1,8,unit=1)
print(reg1.registers)