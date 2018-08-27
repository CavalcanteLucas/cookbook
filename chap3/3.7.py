# Working with Infinity and NaNs

a = float('inf')
b = float('-inf')
c = float('nan')
[a, b, c]

import math
math.isinf(a)
math.isnan(c)


# Discussion

a = float('inf')
a + 45
a * 10
10 / a

a/a
a + b

c + 23
c / 2
c + 2
math.sqrt(c)

d = float('nan')
c == d
c is d
