# Performing I/O Operations on a String

import io

s = io.StringIO()
s.write('Hello World\n')
print('This is a test', file=s)

# Get all of the data writte so far
s.getvalue()

# Wrap a file interface around an existing string
s = io.StringIO('Hello\nWorld\n')
s.read(4)
s.read()

s = io.BytesIO()
s.write(b'binary data')
s.getvalue()
