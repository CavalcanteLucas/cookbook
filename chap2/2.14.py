# Combining and Concatanating Strings

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)
','.join(parts)
''.join(parts)

a = 'Is Chicago'
b = 'Not Chicago?'
a + ' '  + b

print('{} {}'.format(a,b))
print(a + ' ' + b)

a = 'Hello' 'World'
a


# Discussion

# Don't ever do this:
s = ''
for p in parts:
    s += p

data = ['ACME', 50, 91.1]
','.join(str(d) for d in data)

a = 'this'
b = 'is a'
c = 'string'
print(a + ':' + b + ':' + c) # Ugly
print(':'.join([a, b, c]))   # Still ugly
print(a,b,c, sep=':')        # Better


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text = ''.join(sample())
text

for part in sample():
    print(part)


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts=[]
            size=0
    yield ''.join(parts)

for part in combine(sample(), 32768):
    print(part)

