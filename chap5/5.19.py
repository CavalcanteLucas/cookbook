# MAking Temporary Files and Directories

from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')
    
    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
# Temporary file is destroyed

f = TemporaryFile('w+t')
# Use temporary file
# ...
f.close()
# File is destroyed

# line from PC3rd is actually:
# with TemporaryFile('w+t', encoding='utf-8', errors='ignore'
with TemporaryFile('w+t', encoding='utf-8') as f:
    pass


from tempfile import NamedTemporaryFile

with NamedTemporartFile('w+t') as f:
    print('filename is: ', f.name)

# File automatically destroyed

#with NamedTemporaryFile('w+t', delete=False) as f:
#    print('filename is:', f.name)


from tempfile import TemporaryDirectory
with TemporaryDirectory() as dirname:
    print('dirname is: ', dirname)
    # Use the directory
    # ...
# Directory and all contents destroyed


# Discussion

import tempfile
tempfile.mkstemp()
tempfile.mkdtemp()
tempfile.gettempdir()

f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
f.name
