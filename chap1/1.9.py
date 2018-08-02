# Finding Commonalities in Two Dictionaries

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

print(a.keys() - {'z'})

c = {key:a[key] for key in a.keys()}
print(c)

d = {key:a[key] for key in a.keys() - {'z'}}
print(d)

e = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(e)

f = a.values()
print(f)