from collections import deque


def bfs(row, col):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    bfs_q = deque()
    bfs_q.append([row, col])
    visited[row][col] = 1
    
    melting = 0
    
    air = [[0 for _ in range(M)] for _ in range(N)]
    
    while bfs_q:        
        r, c = bfs_q.popleft()
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if 0 <= new_row < N and 0 <= new_col < M:
                if graph[new_row][new_col] == 0 and visited[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col])
                    visited[new_row][new_col] = 1
                
                if graph[new_row][new_col] == 1 and visited[new_row][new_col] == 0:
                    
                    air[new_row][new_col] += 1
    
    for i in range(N):
        for k in range(M):
            if air[i][k] >= 2:
                graph[i][k] = 0
                melting += 1
    
    return melting
    
N, M = map(int, input().split())

graph = [[] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

cheese = []
melting_cnt = 0

res = 0

for i in range(N):
    arr = map(int, input().split())
    
    for idx, k in enumerate(arr):
        if k == 1:
            cheese.append([i, idx])
        
        graph[i].append(k)

while melting_cnt < len(cheese):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    melting_cnt += bfs(0, 0)
    
    res += 1

print(res)