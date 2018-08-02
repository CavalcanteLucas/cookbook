# Mapping Keys to Multiple Values in a Dicionary

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}

print(d)
print(e)

from collections import defaultdict

f = defaultdict(list)
f['a'].append(1)
f['a'].append(2)
f['b'].append(4)
print(f)

g = defaultdict(set)
g['a'].add(1)
g['a'].add(2)
g['b'].add(4)
print(g)

h = {}
h.setdefault('a', []).append(1)
h.setdefault('a', []).append(2)
h.setdefault('b', []).append(4)
print(h)


"""
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
"""