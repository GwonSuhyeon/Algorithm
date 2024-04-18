import sys
from collections import deque


def bfs(row, col):
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, -1], [-1, 1]]
    
    visited = [[0 for _ in range(M)] for _ in range(N)]
        
    bfs_q = deque()
    bfs_q.append([row, col, 0])
    visited[row][col] = 1
    
    while len(bfs_q):
        r, c, dist = bfs_q.popleft()
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if 0 <= new_row < N and 0 <= new_col < M:
                if graph[new_row][new_col] == 0 and visited[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col, dist + 1])
                    visited[new_row][new_col] = 1
                
                elif graph[new_row][new_col] == 1 and visited[new_row][new_col] == 0:
                    visited[new_row][new_col] = 1
                    
                    return dist + 1
    
    return 0

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

res = 0

for row in range(N):
    for col in range(M):
        if graph[row][col] == 0:
            dist = bfs(row, col)
            
            res = max(res, dist)

print(res)