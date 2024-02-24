from collections import deque

n, k = map(int, input().split())

res = ''

remove = []

q = deque()

cnt = 1

for i in range(1, n + 1):
    q.append(i)

while len(q) > 0:
    if cnt < k:
        q.append(q.popleft())
        
        cnt += 1
    
    else:
        remove.append(q.popleft())
        
        cnt = 1
    
for idx, i in enumerate(remove):
    if idx == 0:
        res += f'<{i}'
    
    else:
        res += f', {i}'

res += '>'

print(res)