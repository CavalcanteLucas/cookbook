# Manipulating Pathnames

import os
path = '/User/beazley/Data/data.csv'

# Get the last component of the path
f = os.path.basename(path)
print(f)

# Get the directory name
d = os.path.dirname(path)
print(d)

# Join path components together
j = os.path.join('tmp', 'data', os.path.basename(path))
print(j)

# Expand the user's home directory
path = '~/Data/data.csv'
u = os.path.expanduser(path)
print(u)

# Split the file extensions
s = os.path.splitext(path)
print(s)
