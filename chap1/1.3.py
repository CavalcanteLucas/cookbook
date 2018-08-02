# Keeping the last N Items

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == 'main':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)


q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)


q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)

q.appendleft(4)
print(q)

q.pop()
print(q)

q.popleft()
print(q)
