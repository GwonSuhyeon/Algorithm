import sys
from collections import deque


def bfs(r1, c1):
    global res
    
    direction = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
    
    bfs_q = deque()
    
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[r1][c1] = 1
    
    bfs_q.append([r1, c1, visited.copy(), 0])
    
    while len(bfs_q):
        r, c, visited, move = bfs_q.popleft()
        
        if r == r2 and c == c2:
            res = min(res, move)
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if 0 <= new_row < N and 0 <= new_col < N and visited[new_row][new_col] == 0:
                visited[new_row][new_col] = 1
                bfs_q.append([new_row, new_col, visited.copy(), move + 1])
                
                
input = sys.stdin.readline

N = int(input().rstrip())

r1, c1, r2, c2 = map(int, input().rstrip().split())

res = 999999

bfs(r1, c1)

if res == 999999:
    print(-1)

else:
    print(res)