# Getting a Directory Listing

import os
my_dir1 = ('/home/lucas/python-cookbook/chap5/')
my_dir2 = ('/home/lucas/python-cookbook/')
names1 = os.listdir(my_dir1)


import os.path

# Get all regular files
def get_all_files(some_dir):
    return [name for name in os.listdir(some_dir)
         if os.path.isfile(os.path.join(some_dir, name))]

#print(get_all_files(my_dir1))
#print(get_all_files(my_dir2))

# Get all dirs
def get_all_dirs(some_dir):
    return [name for name in os.listdir(some_dir)
            if os.path.isdir(os.path.join(some_dir, name))]

#print(get_all_dirs(my_dir1))
#print(get_all_dirs(my_dir2))


def get_pyfiles(some_dir):
    return [name for name in os.listdir(some_dir)
            if name.endswith('.py')]

#print(get_pyfiles(my_dir1))
#print(get_pyfiles(my_dir2))


import glob
pyfiles = glob.glob('/home/lucas/python-cookbook/chap5/*.py')
#print(pyfiles)

from fnmatch import fnmatch

def get_pyfiles2(some_dir):
    return [name for name in os.listdir(some_dir)
           if fnmatch(name, '*.py')]

#print(get_pyfiles2(my_dir1))
#print(get_pyfiles2(my_dir2))


# Discussion

# Example of getting a directory liting

import os
import os.path
import glob

pyfiles = glob.glob('*.py')

# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]

#for name, size, mtime in name_sz_date:
#    print(name, size, mtime)

# Alternative: Get fie metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
