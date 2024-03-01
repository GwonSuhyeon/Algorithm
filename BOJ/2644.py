def dfs(x, b):
    global res, isFind
    
    visited[x] = 1
    
    if isFind == True:
        return
    
    res += 1
    
    for i in graph[x]:
        if i == b:
            isFind = True
        
        if visited[i] == 0:
            dfs(i, b)
            
            if isFind == False:
                res -= 1

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

global res, isFind
res = 0
isFind = False

for _ in range(m):
    x, y = map(int, input().split())
    
    graph[x].append(y)
    graph[y].append(x)

dfs(a, b)

if isFind == False:
    print(-1)

else:
    print(res)