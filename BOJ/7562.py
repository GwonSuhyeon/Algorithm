import sys
from collections import deque


def bfs(visited, start_y, start_x, end_y, end_x, I):
    
    direction = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]]
    
    bfs_q = deque()
    bfs_q.append([start_y, start_x, 0])
    visited[start_y][start_x] = 1
    
    while len(bfs_q):
        r, c, move_cnt = bfs_q.popleft()
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if 0 <= new_row < I and 0 <= new_col < I:
                if visited[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col, move_cnt + 1])
                    visited[new_row][new_col] = 1
                                        
                    if new_row == end_y and new_col == end_x:
                        return move_cnt + 1

T = int(input())

for _ in range(T):
    I = int(sys.stdin.readline().rstrip())
    
    start_y, start_x = list(map(int, sys.stdin.readline().rstrip().split()))
    end_y, end_x = list(map(int, sys.stdin.readline().rstrip().split()))
    
    visited = [[0 for _ in range(I)] for _ in range(I)]
    
    if start_y == end_y and start_x == end_x:
        res = 0
    else:
        res = bfs(visited, start_y, start_x, end_y, end_x, I)
    
    print(res)