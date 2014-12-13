import struct
from crcmod import mkCrcFun

crc16xmodem = mkCrcFun(0x11021, rev=False, initCrc=0x0000, xorOut=0x0000)

def calc_crc(data):
    assert len(data) >= 16

    crc = crc16xmodem(data[:4])
    crc = crc16xmodem('\0\0', crc)
    crc = crc16xmodem(data[6:], crc)
    return crc


def check_crc(data):
    assert len(data) >= 16

    crc1 = calc_crc(data)
    crc2 = struct.unpack_from('!H', data, 4)[0]
    return crc1 == crc2


def set_crc(data):
    assert len(data) >= 16

    crc = calc_crc(data)
    return data[:4] + struct.pack('!H', crc) + data[6:]
