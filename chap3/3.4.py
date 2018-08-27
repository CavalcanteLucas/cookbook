# Working with Binary, Octal, and Hexadecimal Integers

x = 1234
bin(x)
oct(x)
hex(x)

format(x,'b')
format(x,'o')
format(x,'x')

x = -1234
format(x, 'b')
format(x, 'o')
format(x, 'x')

format(2**32 + x, 'b')
format(2**32 + x, 'x')

int('4d2', 16)
int('10011010010', 2)


# Discussion

import os
os.chmod('script.py', 0755) # invalid token!
os.chmod('script.py', 0x0755)