# Printing Bad Filenames

def bad_filename1(filename):
    return repr(filename[1:-1])

def bad_filename2(filename):
    import sys
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')

'''
try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))
'''

# Discussion

with open('b\udce4d.txt', 'w') as f:
    f.write('Super Spice!')

import os
files = os.listdir('.')
for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename2(name))


