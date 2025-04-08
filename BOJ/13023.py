import sys

sys.setrecursionlimit(10**6)

def dfs(x, depth):
    global res

    if depth == 4:
        res = 1
        return
    
    if res == 1:
        return
    
    visited[x] = 1

    for node in graph[x]:
        if visited[node] == 0:
            dfs(node, depth + 1)

            if res == 1:
                break
            
    visited[x] = 0

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
visited = [0 for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

res = 0

for i in range(N):
    dfs(i, 0)

    if res == 1:
        break

print(res)