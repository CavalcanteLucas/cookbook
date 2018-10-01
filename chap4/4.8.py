# Skippingn the First Part of an Iterable

s1 = ''
with open('/etc/passwd') as f:
    for line in f:
        # print(line, end='')
        s1 = s1 + line
# print(s1)

s2 = ''
from itertools import dropwhile
with open('/etc/passwd') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')
        s2 = s2 + line
# print(s2)

print(s1 == s2)


from itertools import islice
items = ['a','b','c',1,4,10,15]
for x in islice(items, 3, None):
    # print(x)
    x


# Discussion

with open('/etc/passwd') as f:
    # Skip over initial comments
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    # Process remaining lines
    while line:
        # Replace with useful processing
        # print(line, end='')
        line = next(f, None)

# alternative solution that drops it all throughout the file
# not only the initial cases UNTIL condition is no longer satisfied
with open('/etc/passwd') as f:
    lines = (line for line in f if not line.startswith('p') and not line.startswith('n'))
    for line in lines:
        # print(line, end='')
        line