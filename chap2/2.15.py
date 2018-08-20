# Interpolating Variables in Strings

s = '{name} has {n} messages.'
s.format(name='Guido', n=37)

name = 'Guido'
n = 37
s.format_map(vars())

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
a
s.format_map(vars(a))

# Drawback with format and format_map : they don't deal gracefully with missing args
s.format(name='Guido') # Error

class safesub(dict): # DOUBT
    def __missing__(self, key): # DOUBT
        return '{' + key + '}'

del n
s.format_map(safesub(vars())) # DOUBT


import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals)) # DOUBT
name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))


# Discussion

# Obsolete: 

# name = 'Guido'
# n = 37
# "%(name) has %(n) messages." % vars()

import string
s = string.Template('$name has $n messages.')
s
s.substitute(vars())
