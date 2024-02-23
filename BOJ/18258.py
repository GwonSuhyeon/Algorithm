import sys
from collections import deque

n = int(input())

q = deque()

res = []

for _ in range(n):
    s = sys.stdin.readline().split()
    
    if s[0] == 'push':
        q.append(int(s[1]))
    
    elif s[0] == 'pop':
        if len(q) == 0:
            res.append(-1)
        
        else:
            res.append(q.popleft())
    
    elif s[0] == 'size':
        res.append(len(q))
    
    elif s[0] == 'empty':
        if len(q) == 0:
            res.append(1)
        
        else:
            res.append(0)
    
    elif s[0] == 'front':
        if len(q) == 0:
            res.append(-1)
        
        else:
            res.append(q[0])
    
    elif s[0] == 'back':
        if len(q) == 0:
            res.append(-1)
        
        else:
            res.append(q[-1])

for i in res:
    print(i)