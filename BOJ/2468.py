from collections import deque

def bfs(row, col, height):
    bfs_q = deque()
    bfs_q.append([row, col])
    
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    while len(bfs_q):
        r, c = bfs_q.popleft()
        
        if visited[r][c] == 1:
            continue
        
        visited[r][c] = 1
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if new_row >= 0 and new_row < n and new_col >= 0 and new_col < n:
                if graph[new_row][new_col] > height and visited[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col])

n = int(input())

graph = [[] for _ in range(n)]

maximum = 0

res = 1

for i in range(n):
    s = input().split()
    
    for k in s:
        graph[i].append(int(k))
    
    temp = max(graph[i])
    if maximum < temp:
        maximum = temp

for i in range(1, maximum + 1):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    
    region = 0
    
    for row in range(n):
        for col in range(n):
            if graph[row][col] > i and visited[row][col] == 0:
                bfs(row, col, i)
                
                region += 1
    
    if res < region:
        res = region

print(res)