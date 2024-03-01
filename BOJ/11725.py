import sys

sys.setrecursionlimit(10000000)

def dfs(x):
    visited[x] = 1
    
    for i in graph[x]:
        if visited[i] == 0:
            res[i] = x
            dfs(i)

n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

res = [0 for _ in range(n + 1)]

for _ in range(1, n):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in res[2:]:
    print(i)