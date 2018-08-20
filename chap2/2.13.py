# Aligning Text Strings

text = 'Hello World'
text.ljust(20)
text.rjust(20)
text.center(20)

text.rjust(20,'=')
text.center(20,'*')

format(text, '>20')
format(text, '<20')
format(text, '^20')

format(text, '=>20')
format(text, '*^20')

'{:>10s} {:>10s}'.format('Hello', 'World')

x = 1.2345
format(x, '>10')
format(x, '^10.2f')


# Discussion

# Older:
'%-20s' % text
'%20s' % text