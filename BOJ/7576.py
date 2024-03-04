from collections import deque

def bfs():
    global visit_cnt
    
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    bfs_q = start.copy()
    start.clear()
    
    while len(bfs_q):
        r, c = bfs_q.popleft()
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if new_row >= 0 and new_row < n and new_col >= 0 and new_col < m:
                if graph[new_row][new_col] == 0 and visited[new_row][new_col] == 0:
                    start.append([new_row, new_col])
                    visited[new_row][new_col] = 1
                    visit_cnt += 1
    
m, n = map(int, input().split())

graph = [[] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

global visit_cnt
visit_cnt = 0
less_tomato = False
day = 0

start = deque()

for i in range(n):
    tomato = input().split()
    
    for idx, t in enumerate(tomato):
        if t == '1':
            start.append([i, idx])
            visited[i][idx] = 1
            visit_cnt += 1
        
        elif t == '-1':
            visited[i][idx] = 1
            visit_cnt += 1
        
        elif t == '0':
            less_tomato = True
        
        graph[i].append(int(t))

while len(start):
    if visit_cnt == (m * n):
        break
    
    bfs()
    day += 1

for row in range(n):
    for col in range(m):
        if visited[row][col] == 0:
            day = -1
            break

if less_tomato == False:
    day = 0

print(day)