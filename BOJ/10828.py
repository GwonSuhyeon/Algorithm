n = int(input())

res = []
stack = []

for _ in range(n):
    s = input().split()
    
    if s[0] == 'push':
        stack.append(int(s[1]))
    
    elif s[0] == 'pop':
        if len(stack) == 0:
            res.append(-1)
        
        else:
            res.append(stack[-1])
            stack.pop()
    
    elif s[0] == 'size':
        res.append(len(stack))
    
    elif s[0] == 'empty':
        if len(stack) == 0:
            res.append(1)
        
        else:
            res.append(0)
    
    elif s[0] == 'top':
        if len(stack) == 0:
            res.append(-1)
        
        else:
            res.append(stack[-1])

for i in res:
    print(i)