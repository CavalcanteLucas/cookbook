# Performing Text Operations on Byte Strings

data = b'Hello World'
data[0:5]
data.startswith(b'Hello')
data.split()
data.replace(b'Hello', b'Hello Cruel')

data = bytearray(b'Hello World')
data[0:5]
data.startswith(b'Hello')
data.split()
data.replace(b'Hello', b'Hello cruel')

data = b'FOO:BAR,SPAM'
import re
re.split('[:,]', data) # Error
re.split(b'[:,]', data) # Notice: pattern as bytes


# Discussion

a = 'Hello World'
a[0]
a[1]

b = b'Hello World'
b[0]
b[1]

s = b'Hello World'
print(s)
print(s.decode('ascii'))

b'%10s %10d %10.2f' % (b'ACME', 100, 490.1)
# b'{} {} {}'.format(b'ACME', 100, 490.1) # Error

'{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')


# Write a UTF-8 filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

# Get a dictionary listing
import os
os.listdir('.')  # Text string (names are decoded)
os.listdir(b'.') # Byte string (names left as bytes)