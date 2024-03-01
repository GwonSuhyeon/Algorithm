from collections import deque

def bfs(row, col):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    global region
    region = 0
    
    bfs_q = deque()
    
    bfs_q.append([row, col])
    
    while len(bfs_q):
        r, c = bfs_q.popleft()
        
        if visited[r][c] == 1:
            continue
        
        visited[r][c] = 1
        region += 1
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n:
                if graph[new_row][new_col] == 0 and visited[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col])
    
    res.append(region)

m, n, k = map(int, input().split())

graph = [[0 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]

res = []

global region

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    
    for row in range(y1, y2):
        for col in range(x1, x2):
            graph[row][col] = 1

for row in range(m):
    for col in range(n):
        if graph[row][col] == 0 and visited[row][col] == 0:
            bfs(row, col)

res = sorted(res)

print(len(res))

for i in res:
    print(i, end=' ')