# Iterating in Reverse

a = [1,2,3,4]
for x in reversed(a):
    print(x)

# Discussion

class Countdown: # how to use it?
    def __init__(self, start):
        self.start = start
    
    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n = -1

    # Reversed iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

# Print a file backwards
f = open('4.4.py')
for line in reversed(list(f)):
    print(line, end='')

# python