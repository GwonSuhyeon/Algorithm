from collections import deque

t = int(input())

res = []

for _ in range(t):
    n, m = map(int, input().split())
    p = list(input().split())
    
    paper = deque()
    priority = deque()
    
    cnt = 0
    
    for i in range(n):
        paper.append(i)
        priority.append(int(p[i]))
    
    while True:
        maximum = max(priority)
        
        if priority[0] < maximum:
            paper.append(paper.popleft())
            priority.append(priority.popleft())
        
        elif priority[0] == maximum:
            if paper[0] == m:
                cnt += 1
                break
            
            else:
                paper.popleft()
                priority.popleft()
                
                cnt += 1
    
    res.append(cnt)

for i in res:
    print(i)