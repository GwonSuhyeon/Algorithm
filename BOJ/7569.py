from collections import deque

def bfs():
    global visit_cnt
    
    direction = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
    
    bfs_q = start.copy()
    start.clear()
    
    while len(bfs_q):
        height, row, col = bfs_q.popleft()
        
        for z, y, x in direction:
            new_height, new_row, new_col = height + z, row + y, col + x
            
            if new_height >= 0 and new_height < h and new_row >= 0 and new_row < n and new_col >= 0 and new_col < m:
                if graph[new_height][new_row][new_col] == 0 and visited[new_height][new_row][new_col] == 0:
                    start.append([new_height, new_row, new_col])
                    visited[new_height][new_row][new_col] = 1
                    visit_cnt += 1

m, n, h = map(int, input().split())

graph = [[[] for _ in range(n)] for _ in range(h)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

global visit_cnt
visit_cnt = 0

start = deque()

bad_tomato = 0
day = 0

for i in range(h):
    for k in range(n):
        values = input().split()
        
        for idx, v in enumerate(values):
            if v == '0':
                bad_tomato += 1
            
            elif v == '1':
                start.append([i, k, idx])
            
            graph[i][k].append(int(v))

if bad_tomato > 0:
    while len(start):
        bfs()
        
        if len(start) > 0:
            day += 1

    if visit_cnt < bad_tomato:
        day = -1

else:
    day = 0

print(day)