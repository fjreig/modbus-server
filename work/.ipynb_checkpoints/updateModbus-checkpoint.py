from pymodbus.client.sync import ModbusTcpClient

address = 2
value = 12
unitId = 1
host = "127.0.0.1"
port = 5020

cliente = ModbusTcpClient(host, port)
cliente.connect()
cliente.write_register(address, value, init= unitId)