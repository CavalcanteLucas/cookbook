# Splitting Strings on Any of Multiple Delimiters

line = 'asdf fjdk; afed, fjek,asdf,    foo'
import re
re.split(r'[;,\s]\s*', line)

# Discussion

fields = re.split(r'(;|,|\s)\s*', line)
fields

values = fields[::2]
values
delimiters = fields[1::2] + ['']
delimiters

# Reform the line using the same delimiters
''.join(v + d for v,d in zip(values, delimiters))

re.split(r'(?:,|;|\s)\s*', line)
