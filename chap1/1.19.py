# Transforming and Reducing Data at the Same Time

# Elegant way to combine data reduction and a transformation:
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# Determine if any .py files exist in a directory
import os
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('there be python!')
else:
    print('sorry, no python')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structures
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65},
]
min_share = min(s['shares'] for s in portfolio)

# DISCUSSION

s = sum((x*x for x in nums)) # Pass generator-expr as arguments
s = sum(x*x for x in nums)   # More elegant syntax

# useless extra-step creating a list instead of a generator
num = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])

# Original: Returns 20
min_shares = min(s['shares'] for s in portfolio)
min_shares
# Alternative:
min_shares = min(portfolio, key=lambda s: s['shares'])
min_shares