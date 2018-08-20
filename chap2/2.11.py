# Stripping Unwanted Characters from Strings

# Whitespace stripping
s = '   hello world  \n'
s.strip()
s.lstrip()
s.rstrip()

# Character stripping
t = '------hello====='
t.lstrip('-')
t.strip('-=')


# Discussion

s = '  hello     world  \n'
s = s.strip()
s

s.replace(' ', '')
import re
re.sub(r'\s+', ' ', s)