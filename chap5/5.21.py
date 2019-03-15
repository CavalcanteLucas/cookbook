# Serializing Python Objects

import pickle

data = [1,2,3] # Some Python object
f = open('somefile', 'wb')
pickle.dump(data,f)

s = pickle.dumps(data)

# Restore from a file
f = open('somefile', 'rb')
data = pickle.load(f)
print(data)

# Restore from a string
data = pickle.loads(s)
print(data)


# Discussion

f = open('somedata', 'wb')
pickle.dump([1,2,3], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('somedata', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))

import math
pickle.dumps(math.cos)


import countdown
c = countdown.Countdown(10)

f = open('cstate', 'wb')
import pickle
pickle.dump(c,f)
f.close()

f = open('cstate', 'rb')
pickle.load(f)

