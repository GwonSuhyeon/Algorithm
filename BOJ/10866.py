from collections import deque

n = int(input())

q = deque()

res = []

for _ in range(n):
    s = input().split()
    
    if s[0] == 'push_front':
        q.appendleft(s[1])
    
    elif s[0] == 'push_back':
        q.append(s[1])
    
    elif s[0] == 'pop_front':
        if len(q) == 0:
            res.append(-1)
        
        else:
            res.append(q.popleft())
    
    elif s[0] == 'pop_back':
        if len(q) == 0:
            res.append(-1)
        
        else:
            res.append(q.pop())
    
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