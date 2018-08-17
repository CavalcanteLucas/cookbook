# Matching Text at the Start or End of a String

filename = 'spam.txt'
filename.endswith('.txt')
filename.startswith('file:')

url = 'http://www.python.org'
url.startswith('http')

import os
filenames = os.listdir('.')
filenames
[name for name in filenames if name.endswith(('1', '2'))]
any(name.endswith('8') for name in filenames)

from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:', 'ftp:']
url = 'http://www.python.org'
#url.startswith(choices) # Error
url.startswith(tuple(choices))

# Discussion

filename = 'spam.txt'
filename[-4:] == '.txt'

url = 'http://www.python.org'
url[:5] == 'http:' or url[:6] == 'https' or url[:4] == 'ftp:'

import re
url = 'http://www.python.org'
re.match('http:|https:|ftp:', url)

# if any(name.endswith(('.c', ',h')) for name in listdir(dirname)):
#    ...