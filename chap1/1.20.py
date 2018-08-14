# Combinig Multiple Mappings into a Single Mapping

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap
c = ChainMap(a,b)
c
print(c['x'])   # Outputs 1 (from a)
print(c['y'])   # Outputs 2 (from b)
print(c['z'])   # Outputs 3 (from a)

# DISCUSSION

len(c)
list(c.keys())
list(c.values())

c['z'] = 10
c
c['w'] = 40
c
del c['x']
c
a
# del c['y']    # Error

values = ChainMap()
values['x'] = 1
values = values.new_child() # Add a new mapping
values
values['x'] = 2
values = values.new_child()
values
values['x'] = 3 
values
values['x']
values = values.parents # Discard last mapping
values
values = values.parents
values
values['x']

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged
merged.update(a)
merged
merged['x']
merged['y']
merged['z']
a['x'] = 13
merged['x']

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = ChainMap(a,b)
merged['x']
a['x'] = 42
merged['x']