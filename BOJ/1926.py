from collections import deque

def bfs(row, col):
    bfs_q = deque()
    bfs_q.append([row, col])
    
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    region = 0
    
    while len(bfs_q):
        r, c = bfs_q.popleft()
        
        if visited[r][c] == 1:
            continue
        
        visited[r][c] = 1
        region += 1
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if new_row >= 0 and new_row < n and new_col >= 0 and new_col < m:
                if graph[new_row][new_col] == 1 and visited[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col])
    
    return region
    

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    picture = input().split()
    
    for p in picture:
        graph[i].append(int(p))

cnt = 0
size = 0

for row in range(n):
    for col in range(m):
        if graph[row][col] == 1 and visited[row][col] == 0:
            region = bfs(row, col)
            
            cnt += 1
            size = max(size, region)

print(cnt)
print(size)