# Mapping Names to Sequence Elements]

from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
sub
sub.addr
sub.joined

len(sub)
addr, joined = sub
addr
joined

def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def comput_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

# DISCUSSION

s = Stock('ACME', 100, 123.45)
s
# s.shares = 75 # this is an error
s._replace(shares=75)
s

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert from dictionart to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
dict_to_stock(a)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
dict_to_stock(b)