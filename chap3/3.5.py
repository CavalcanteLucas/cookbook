# Packing and Unpacking Large Integers from Bytes

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
len(data)
int.from_bytes(data, 'little')
int.from_bytes(data, 'big')

x = 9452284252074728448711772783387188
x.to_bytes(16, 'big')
x.to_bytes(16, 'little')


# Discussion

data
import struct
hi, lo = struct.unpack('>QQ', data)
(hi << 64) + lo # shifts 64 bits to the left
hi

x = 0x01020304
x.to_bytes(4, 'big')
x.to_bytes(4, 'little')

x = 523 ** 23
x
x.to_bytes(16,'little') # Overflow
x.bit_length()
nbytes, rem = divmod(x.bit_length(), 8)
nbytes
rem
if rem:
    nbytes += 1
x.to_bytes(nbytes, 'little')

