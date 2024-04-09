import sys
from collections import deque, defaultdict


def bfs1(row, col, color):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    bfs_q = deque()
    bfs_q.append([row, col])
    visited1[row][col] = 1
    
    while bfs_q:
        r, c = bfs_q.popleft()
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if 0 <= new_row < N and 0 <= new_col < N:
                if graph[new_row][new_col] == color and visited1[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col])
                    visited1[new_row][new_col] = 1
    
    color_region1[color] += 1

def bfs2(row, col, color):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    bfs_q = deque()
    bfs_q.append([row, col])
    visited2[row][col] = 1
    
    while bfs_q:
        r, c = bfs_q.popleft()
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if 0 <= new_row < N and 0 <= new_col < N:
                if color == 'B':
                    if graph[new_row][new_col] == color and visited2[new_row][new_col] == 0:
                        bfs_q.append([new_row, new_col])
                        visited2[new_row][new_col] = 1
                
                else:
                    if (graph[new_row][new_col] == 'R' or graph[new_row][new_col] == 'G') and visited2[new_row][new_col] == 0:
                        bfs_q.append([new_row, new_col])
                        visited2[new_row][new_col] = 1
    
    if color == 'G':
        color = 'R'
    
    color_region2[color] += 1

N = int(sys.stdin.readline().rstrip())

graph = []

visited1 = [[0 for _ in range(N)] for _ in range(N)]
visited2 = [[0 for _ in range(N)] for _ in range(N)]

color_region1 = defaultdict(int)
color_region2 = defaultdict(int)

for _ in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

for row in range(N):
    for col in range(N):
        if visited1[row][col] == 0:
            bfs1(row, col, graph[row][col])
        
        if visited2[row][col] == 0:
            bfs2(row, col, graph[row][col])

print(sum(color_region1.values()), sum(color_region2.values()))