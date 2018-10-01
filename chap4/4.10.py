# Iterating Over the Index-Value Pairs of a Sequence

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    # print(idx, val)
    val

for idx, val in enumerate(my_list, 1):
    # print(idx, val)
    val

def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            print(fields)
            try:
                fields
                # count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))

# parse_data('4.9.py')

from collections import defaultdict
word_summary = defaultdict(list)

with open('4.9.py', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    # Create a list of words in current line
    # print(idx, line, end='')
    words = [w.strip() for w in line.split()]
    # print(words)
    for word in words:
        word_summary[word].append(idx)


# print(word_summary)


# Discussion

lineno = 1
with open('4.9.py', 'r') as f:
    for line in f:
        # Process line
        lineno += 1
# print(lineno)

with open('4.9.py', 'r') as f:
    for lineno, line in enumerate(f):
        # print(lineno, line, end='')
        line


data = [(1,2), (3,4), (5,6), (7,8)]

# Correct!
for n, (x, y) in enumerate(data):
    # print(n, x, y)
    n

# Error!
# for n, x, y in enumerate(data):
    # print(n, x, y)


