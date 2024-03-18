from collections import deque
import sys

def bfs(row, col):
    
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    bfs_q = deque()
    visited[row][col][0] = 1
    bfs_q.append([row, col, 1, 0])
    
    while len(bfs_q):
        r, c, move, broken = bfs_q.popleft()
        
        if r == (N - 1) and c == (M - 1):
            res.append(move)
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if new_row >= 0 and new_row < N and new_col >= 0 and new_col < M:
                if graph[new_row][new_col] == 0 and visited[new_row][new_col][broken] == 0:
                    visited[new_row][new_col][broken] = 1
                    bfs_q.append([new_row, new_col, move + 1, broken])
                    
                elif graph[new_row][new_col] == 1 and broken == 0:
                    visited[new_row][new_col][broken] = 1
                    bfs_q.append([new_row, new_col, move + 1, 1])

N, M = map(int, input().split())

graph = []
visited = []
res = []

for _ in range(N):
    graph.append([int(i) for i in list(sys.stdin.readline().rstrip())])
    visited.append([[0, 0] for _ in range(M)])

bfs(0, 0)

if len(res) == 0:
    print(-1)

else:
    print(min(res))