import sys

sys.setrecursionlimit(1000000)

def dfs(row, col):
    visited[row][col] = 1
    
    for r, c in direction:
        new_row, new_col = row + r, col + c
        if new_row >= 0 and new_row < n and new_col >= 0 and new_col < m:
            if field[new_row][new_col] == 1 and visited[new_row][new_col] == 0:
                dfs(new_row, new_col)

t = int(input())

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

res = []

for _ in range(t):
    m, n, k = map(int, input().split())
    
    cnt = 0
    
    field = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        col, row = map(int, input().split())
        
        field[row][col] = 1
    
    for row in range(n):
        for col in range(m):
            if field[row][col] == 1 and visited[row][col] == 0:
                cnt += 1
                dfs(row, col)
    
    res.append(cnt)

for i in res:
    print(i)