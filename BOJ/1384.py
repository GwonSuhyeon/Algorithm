from collections import deque

res = []

while True:
    
    n = int(input())
    
    if n == 0:
        break
    
    names = []
    msg = []
    group = []
    
    for _ in range(n):
        s = input().split()
        
        names.append(s[0])
        msg.append(s[1:])
    
    for i, m in enumerate(msg):
        if m.count('N') > 0:
            for k in range(len(m)):
                if m[k] == 'N':
                    idx = i - (k + 1)
                    group.append(f'{names[idx]} was nasty about {names[i]}')

    if len(group) == 0:
        group.append('Nobody was nasty')
    
    res.append(group)

for i, group in enumerate(res):
    print(f'Group {i + 1}')
    
    for g in group:
        print(g)
    
    if i < (len(res) - 1):
        print()