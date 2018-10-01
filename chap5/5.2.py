# Printing to a File

with open('somefile.txt', 'wt') as f:
    print('Hello World!', file=f)
