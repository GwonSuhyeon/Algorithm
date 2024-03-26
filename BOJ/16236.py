from collections import deque


def bfs(dist_sum):
    
    global shark_size, shark_y, shark_x, eat
    
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    fish = []
    
    bfs_q = deque()
    bfs_q.append([shark_y, shark_x, dist_sum])
    visited[shark_y][shark_x] = 1
    
    while len(bfs_q):
        r, c, dist = bfs_q.popleft()
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if 0 <= new_row < N and 0 <= new_col < N:
                if graph[new_row][new_col] <= shark_size and visited[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col, dist + 1])
                    visited[new_row][new_col] = 1
                    
                    if 0 < graph[new_row][new_col] < shark_size:
                        fish.append([new_row, new_col, dist + 1])
    
    fish = sorted(fish, key=lambda x : (x[2], x[0], x[1]))
    
    if len(fish) > 0:
        r, c, dist = fish[0]
        graph[r][c] = 0
        shark_y, shark_x = r, c
        
        eat += 1
        
        if eat == shark_size:
            eat = 0
            shark_size += 1
        
        return dist
    
    else:
        return -1


N = int(input())

graph = [[] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

dist_sum = 0
res = 0

global shark_size, shark_y, shark_x, eat
shark_size = 2
eat = 0

for i in range(N):
    for idx, k in enumerate(input().split()):
        if int(k) == 9:
            shark_y = i
            shark_x = idx
            
            graph[i].append(0)
        
        else:
            graph[i].append(int(k))

while True:
    
    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    dist_sum = bfs(dist_sum)
    
    if dist_sum > 0:
        res = dist_sum
        
    else:
        break

print(res)