def back_tracking(part):

    if len(part) == M:
        res.append(part.copy())
        
        return
    
    for i in range(1, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            
            p = part.copy()
            p.append(i)
            
            back_tracking(p)
            
            visited[i] = 0

N, M = map(int, input().split())

arr = [i for i in range(N + 1)]
visited = [0 for _ in range(N + 1)]

res = []

back_tracking([])

for i in res:
    for k in i:
        print(k, end=' ')
    print()