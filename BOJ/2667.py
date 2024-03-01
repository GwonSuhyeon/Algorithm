import sys

sys.setrecursionlimit(10000000)

def dfs(row, col):
    visited[row][col] = 1
    
    global house
    house += 1
    
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    for r, c in direction:
        new_row = row + r
        new_col = col + c
        
        if new_row >= 0 and new_row < n and new_col >= 0 and new_col < n:
            if graph[new_row][new_col] == 1 and visited[new_row][new_col] == 0:
                dfs(new_row, new_col)

n = int(input())

graph = [[] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

global house
group = 0
res = []

for i in range(n):
    s = list(input())
    
    for k in s:
        graph[i].append(int(k))

for row in range(n):
    for col in range(n):
        if graph[row][col] == 1 and visited[row][col] == 0:
            house = 0
            
            dfs(row, col)
            
            group += 1
            res.append(house)

res = sorted(res)

print(group)
for i in res:
    print(i)