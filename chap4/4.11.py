# Iterating Over Multiple Sequences Simultaneously 

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    # print(x, y)
    x

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a, b):
    # print(i)
    i

from itertools import zip_longest
for i in zip_longest(a,b):
    # print(i)
    i

for i in zip_longest(a,b, fillvalue=0):
    # print(i)
    i


# Discussion

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

s = dict(zip(headers, values))

for name, val in zip(headers, values):
    # print(name, '=', val)
    name

a = [1,2,3]
b = [10,11,12]
c = ['x', 'y', 'z']

for i in zip(a, b, c):
    # print(i)
    i

print(zip(a,b))
print(list(zip(a,b)))

