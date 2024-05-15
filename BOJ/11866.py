import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

queue = deque()

for i in range(1, N + 1):
    queue.append(i)

res = []

while len(res) < N:
    for _ in range(K - 1):
        queue.append(queue.popleft())
    
    res.append(queue.popleft())

print('<', end='')
for idx, i in enumerate(res):
    if idx > 0:
        print(f', {i}', end='')
        
    else:
        print(i, end='')
print('>', end='')