# Filtering Sequence Elements

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n > 0]
[n for n in mylist if n < 0]

pos = (n for n in mylist if n > 0)
pos
for x in pos:
    print(x)

#

import math
[math.sqrt(n) for n in mylist if n > 0]

clip_neg = [n if n > 0 else 0 for n in mylist]
clip_neg
clip_pos = [n if n < 0 else 0 for n in mylist]
clip_pos

address = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '5122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BRODWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
more5

list(compress(address, more5))
