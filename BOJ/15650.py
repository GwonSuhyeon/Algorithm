def dfs(start, part):
    
    if len(part) == M and part not in res:
        res.append(part.copy())
        
        return
    
    for i in range(start, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            
            p = part.copy()
            p.append(i)
            
            dfs(i + 1, p)
            
            visited[i] = 0
            
            
    
N, M = map(int, input().split())

arr = [i for i in range(N + 1)]
visited = [0 for _ in range(N + 1)]

res = []

for i in arr[1:]:
    visited = [0 for _ in range(N + 1)]
    dfs(i, [])

for i in res:
    for k in i:
        print(k, end=' ')
    print()