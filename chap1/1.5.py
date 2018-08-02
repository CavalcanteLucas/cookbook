# Implementing a Priority Queue

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return('Item(%s)' % self.name)


q = PriorityQueue()
print(q)
q.push(Item('foo'), 1)
print(q)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())  

a = Item('foo')
b = Item('bar')
# a < b
a = (1, Item('foo'))
b = (4, Item('bar'))
print(a < b)
c = (1, Item('grok'))
# print(a < c)
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a<b)
print(a<c)
print(b<c)