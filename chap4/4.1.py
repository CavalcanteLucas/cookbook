# Manually Consuming an Iterator

with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass


with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')


# Discussion

items = [1, 2, 3]
# Get the iterator
it = iter(items)    # Invokes items.__iter__()
# Run the iterator
next(it)            # Invokes it.__next__()
next(it)
next(it)
next(it)