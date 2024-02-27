from collections import deque

def dfs(x):
    nodes = sorted(grape[x])
    
    for node in nodes:
        if visited[node] == 0:
            res[0].append(node)
            visited[node] = 1
            dfs(node)

def bfs(x):
    bfs_q = deque()
    
    nodes = sorted(grape[x])
    
    for node in nodes:
        bfs_q.append(node)
    
    while True:
        if len(bfs_q) == 0:
            break
        
        node = bfs_q.popleft()
        
        if visited[node] == 0:
            res[1].append(node)
            visited[node] = 1
            
            for i in sorted(grape[node]):
                bfs_q.append(i)

n, m, v = map(int, input().split())

res = [[], []]

grape = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    
    grape[a].append(b)
    grape[b].append(a)

visited = [0 for _ in range(n + 1)]
res[0].append(v)
visited[v] = 1
dfs(v)

visited = [0 for _ in range(n + 1)]
res[1].append(v)
visited[v] = 1
bfs(v)

for i in res[0]:
    print(i, end=' ')

print()

for i in res[1]:
    print(i, end=' ')