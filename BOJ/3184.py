from collections import deque

def bfs(row, col):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    bfs_q = deque()
    bfs_q.append([row, col])
    
    visited[row][col] = 1
    
    o, v = 0, 0
    
    if graph[row][col] == 'o':
        o += 1
    
    elif graph[row][col] == 'v':
        v += 1
    
    while len(bfs_q):
        curr_r, curr_c = bfs_q.popleft()
        
        for y, x in direction:
            new_row, new_col = curr_r + y, curr_c + x
            
            if new_row >= 0 and new_row < r and new_col >= 0 and new_col < c:
                if graph[new_row][new_col] != '#' and visited[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col])
                    visited[new_row][new_col] = 1
                    
                    if graph[new_row][new_col] == 'o':
                        o += 1
                    
                    elif graph[new_row][new_col] == 'v':
                        v += 1
    
    if o > v:
        res[0] += o
    
    else:
        res[1] += v

r, c = map(int, input().split())

graph = [[] for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]

res = [0, 0]

for i in range(r):
    field = list(input())
    
    for f in field:
        graph[i].append(f)

for row in range(r):
    for col in range(c):
        if graph[row][col] != '#' and visited[row][col] == 0:
            bfs(row, col)

print(f'{res[0]} {res[1]}')