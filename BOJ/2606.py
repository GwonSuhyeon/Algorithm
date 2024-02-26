from collections import deque

def dfs(x):
    nodes = grape[x]
    
    for node in nodes:
        if visited[node] == 0:
            visited[node] = 1
            
            dfs(node)
            
            res.append(node)

computer = int(input())
connect = int(input())

grape = [[] for _ in range(computer + 1)]

for _ in range(connect):
    a, b = map(int, input().split())
    
    grape[a].append(b)
    grape[b].append(a)

visited = [0 for _ in range(computer + 1)]

res = []

visited[1] = 1
dfs(1)  

print(len(res))