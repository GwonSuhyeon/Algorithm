import sys

sys.setrecursionlimit(10000000)

def dfs(row, col):
    visited[row][col] = 1
    
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
    
    for dy, dx in direction:
        new_row = row + dy
        new_col = col + dx
        
        if new_row >= 0 and new_row < h and new_col >= 0 and new_col < w:
            if graph[new_row][new_col] == 1 and visited[new_row][new_col] == 0:
                dfs(new_row, new_col)
    
res = []

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    graph = [[0 for _ in range(w)] for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    
    cnt = 0
    
    for i in range(h):
        m = list(input().split())
        
        for idx, k in enumerate(m):
            graph[i][idx] = int(k)
    
    for row in range(h):
        for col in range(w):
            if graph[row][col] == 1 and visited[row][col] == 0:
                dfs(row, col)
                cnt += 1
    
    res.append(cnt)

for i in res:
    print(i)