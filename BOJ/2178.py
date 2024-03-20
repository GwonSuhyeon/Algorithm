from collections import deque


def bfs():
    
    global res
    
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    bfs_q = deque()
    bfs_q.append([0, 0])
    
    while len(bfs_q):
        r, c = bfs_q.popleft()
        
        if r == (N - 1) and c == (M - 1):
            res = graph[r][c]
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if new_row >= 0 and new_row < N and new_col >= 0 and new_col < M:
                if graph[new_row][new_col] == 1:
                    graph[new_row][new_col] = graph[r][c] + 1
                    bfs_q.append([new_row, new_col])
    
N, M = map(int, input().split())

graph = []
global res

for _ in range(N):
    graph.append(list(map(int, input())))

bfs()

print(res)