import struct

def int_to_uint(value):
    return struct.unpack('<H',struct.pack('<h',value))[0]

def uint_to_int(value):
    return struct.unpack('<h',struct.pack('<H',value))[0]

def int16_to_two_uint8(value):
    return struct.unpack('<BB', struct.pack('<h', value))

def two_uint8_to_int16(byte0, byte1):
    return struct.unpack('<h', struct.pack('<BB', byte0, byte1))[0]

def int32_to_four_uint8(value):
    return struct.unpack('<BBBB', struct.pack('<i', value))

def four_uint8_to_int32(byte0, byte1, byte2, byte3):
    return struct.unpack('<i', struct.pack('<BBBB', byte0, byte1, byte2, byte3))[0]