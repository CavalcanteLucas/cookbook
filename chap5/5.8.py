# Iterating Over Fixed-Sized Records

from functools import partial

RECORD_SIZE = 2

with open('somefile.bin', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)