# Reading Binary Data into a Mutable Buffer

import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

#Write a sampe file
with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
print(buf)

buf[0:5] = b'Hallo'
print(buf)

# Discussion

record_size = 32	# Size of each record (ajust value)

buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
        # Use the content of buf
        print(n)

print(buf)
bytearray(b'Hello World')
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)
m2[:] = b'WORLD'
print(buf)
bytearray(b'Hello WORLD')
