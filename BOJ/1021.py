import sys
from collections import deque


input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

queue = deque()
arr = list(map(int, input().rstrip().split()))

res = 0

for i in range(1, N + 1):
    queue.append(i)

for i in arr:
    if i == queue[0]:
        queue.popleft()
    
    else:
        cw, ccw = 0, 0
        
        while i != queue[0]:
            queue.appendleft(queue.pop())
            cw += 1
        
        for _ in range(cw):
            queue.append(queue.popleft())
        
        while i != queue[0]:
            queue.append(queue.popleft())
            ccw += 1
        
        if cw < ccw:
            for _ in range(cw + ccw):
                queue.appendleft(queue.pop())
            
        queue.popleft()
        
        res += min(cw, ccw)

print(res)