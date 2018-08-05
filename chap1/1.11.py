# Naming a Slice


######    0123456789012345678901234567890123456789012345678901234567890
record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])
print(cost)

SHARES = slice(20,32)
PRICE = slice(40,48)

cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

#

items = [0,1,2,3,4,5,6]
a = slice(2,4)
items[2:4]
items[a]
items[a] = [10,11]
items
del items[a]
items

a = slice(10,50,2)
a.start
a.stop
a.step

# s = 'HelloWorld'
# a.indices(len(s)) #should be (5,10,2) ?
# for i in range(*a.indices(len(s))):
#     print(s[i])




