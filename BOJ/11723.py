import sys

m = int(input())

S = set()

for _ in range(m):
    s = sys.stdin.readline().rstrip().split()
    
    operator = s[0]
    value = 0
    
    if operator != 'all' and operator != 'empty':
        value = int(s[1])
    
    if operator == 'add':
        if value not in S:
            S.add(value)
    
    elif operator == 'remove':
        if value in S:
            S.remove(value)
    
    elif operator == 'check':
        if value in S:
            print(1)
        
        else:
            print(0)
    
    elif operator == 'toggle':
        if value in S:
            S.remove(value)
        
        else:
            S.add(value)
    
    elif operator == 'all':
        S = {i for i in range(1, 21)}
    
    elif operator == 'empty':
        S.clear()