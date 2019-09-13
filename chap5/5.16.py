# Adding or Changing the Encoding of an Already Open File

import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
#print(text)

import sys
#print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
#print(sys.stdout.encoding)


# Discussion
f = open('sample.txt', 'w')
#print(f)
#print(f.buffer)
#print(f.buffer.raw)

# this should error:
#print(f)
#f = io.TextIOWrapper(f.buffer, encoding='latin-1')
#print(f)
#f.write('Hello')

# this should error too
f = open('sample.txt', 'w')
#print(f)
b = f.detach()
b
#f.write('asdf')

f = io.TextIOWrapper(b, encoding='latin-1')
print(f)

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii', errors='xmlcharrefreplace')
print('Jalape\u00f1o')
