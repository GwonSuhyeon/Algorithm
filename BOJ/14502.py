from collections import deque

def bfs(row, col):
    global virus_region
    
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    bfs_q = deque()
    bfs_q.append([row, col])
    visited[row][col] = 1
    
    while len(bfs_q):
        r, c = bfs_q.popleft()
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if new_row >= 0 and new_row < n and new_col >= 0 and new_col < m:
                if graph[new_row][new_col] == 0 and visited[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col])
                    visited[new_row][new_col] = 1
                    virus_region += 1

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
blank = []
virus = []

global virus_region
safe_region = 0

maximum = 0

for i in range(n):
    values = input().split()
    
    for idx, v in enumerate(values):
        if v == '0':
            blank.append([i, idx])
            safe_region += 1
        
        elif v == '2':
            virus.append([i, idx])
        
        graph[i].append(int(v))

for i in range(0, len(blank) - 2):
    for k in range(i + 1, len(blank) - 1):
        for j in range(k + 1, len(blank)):
            p1_y, p1_x = blank[i]
            p2_y, p2_x = blank[k]
            p3_y, p3_x = blank[j]
            
            graph[p1_y][p1_x] = 1
            graph[p2_y][p2_x] = 1
            graph[p3_y][p3_x] = 1
            
            visited = [[0 for _ in range(m)] for _ in range(n)]
            virus_region = 0
            
            for row, col in virus:
                bfs(row, col)
            
            graph[p1_y][p1_x] = 0
            graph[p2_y][p2_x] = 0
            graph[p3_y][p3_x] = 0
            
            maximum = max(maximum, (safe_region - 3) - virus_region)

print(maximum)