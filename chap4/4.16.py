# Replacing Infinite while Loops with an Iterator

CHUNKSIZE = 8192

import sys
f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)