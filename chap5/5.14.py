# Bypassing Filename Encoding

import sys
print(sys.getfilesystemencoding())

# Write a file using a unicode filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spice!')

# Directory listing (decoded)
import os
print(os.listdir('.'))

# Directory listing (row)
print(os.listdir(b'.'))

# Open file with raw filename
with open(b'jalape\xc3\xb1o.txt') as f:
    print(f.read())
