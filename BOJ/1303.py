from collections import deque

def bfs(row, col, type):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    w, b = 0, 0
    
    bfs_q = deque()
    bfs_q.append([row, col])
    visited[row][col] = 1
    
    if type == 'W':
        w += 1
    
    elif type == 'B':
        b += 1
    
    while len(bfs_q):
        r, c = bfs_q.popleft()
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n:
                if graph[new_row][new_col] == type and visited[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col])
                    visited[new_row][new_col] += 1
                    
                    if type == 'W':
                        w += 1
                    
                    elif type == 'B':
                        b += 1
    
    return w, b

n, m = map(int, input().split())

graph = [[] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

res = [0, 0]

for i in range(m):
    army = list(input())
    
    for a in army:
        graph[i].append(a)

for row in range(m):
    for col in range(n):
        if visited[row][col] == 0:
            w, b = bfs(row, col, graph[row][col])
            
            if w > 0:
                res[0] += w**2
            
            if b > 0:
                res[1] += b**2

print(f'{res[0]} {res[1]}')