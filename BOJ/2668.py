import sys

sys.setrecursionlimit(100000000)


def dfs(node):
    cycle.append(node)
    
    for i in graph[node]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
        
        else:
            if i == cycle[0]:
                for k in list(set(cycle)):
                    res.append(k)

            else:
                for k in list(set(cycle[1:])):
                    visited[k] = 0

input = sys.stdin.readline

N = int(input().rstrip())

graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i].append(int(input().rstrip()))

visited = [0 for _ in range(N + 1)]

cycle = []
res = []

for i in range(1, N + 1):
    if visited[i] == 0:
        visited[i] = 1
        dfs(i)
        cycle.clear()

res = sorted(res)

print(len(res))
for i in res:
    print(i)