# Formatting Numbers for Output


x = 1234.56789

# Two decimal places of accuracy
format(x, '0.2f')

# Right justified in 10 chars, one-digit accuracy
format(x, '>10.1f')

# Left justified
format(x, '<10.1f')

# Centered
format(x, '^10.1f')

# Inclusion of thousands separator
format(x, ',')
format(x, '0,.1f')

format(x, 'e')
format(x, '0.2E')

'The value is {:0,.2f}'.format(x)


# Discussion

x
format(x, '0.1f')
format(-x, '0.1f')


swap_separators = { ord('.'):',', ord(','):'.' }
format(x, ',').translate(swap_separators)

'%0.2f' % x
'%10.1f' % x
'%-10.1f' % x
