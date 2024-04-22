import sys
from collections import deque


def bfs(row, col):
    
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    
    bfs_q = deque()
    bfs_q.append([row, col])
    visited[row][col] = 1
    
    block_color = graph[row][col]
    block_cnt = 1
    rainbow_cnt = 0
    rainbow_block = []
    center_block = [999, 999]
    
    group = [[row, col]]
    
    if graph[row][col] != 0:
        center_block[0] = row
        center_block[1] = col
    
    while len(bfs_q):
        r, c = bfs_q.popleft()
        
        for y, x in direction:
            new_row, new_col = r + y, c + x
            
            if 0 <= new_row < N and 0 <= new_col < N:
                if (graph[new_row][new_col] == block_color or graph[new_row][new_col] == 0) and visited[new_row][new_col] == 0:
                    bfs_q.append([new_row, new_col])
                    group.append([new_row, new_col])
                    visited[new_row][new_col] = 1
                    block_cnt += 1
                    
                    if graph[new_row][new_col] == 0:
                        rainbow_cnt += 1
                        rainbow_block.append([new_row, new_col])
                    
                    if 0 < graph[new_row][new_col] <= M:
                        if new_row < center_block[0]:
                            center_block[0] = new_row
                            center_block[1] = new_col
                        
                        elif new_row == center_block[0]:
                            if new_col < center_block[1]:
                                center_block[0] = new_row
                                center_block[1] = new_col

    if block_cnt - rainbow_cnt < 1:
        return [], [], [], 0
    
    return group, center_block, rainbow_block, rainbow_cnt


def gravity():
    for col in range(N):
        blank = N - 1
        
        while True:
            isFind = False
            
            for row in range(N - 1, -1, -1):
                if graph[row][col] == 999:
                    blank = row
            
                    for row in range(blank, -1, -1):
                        if graph[row][col] == -1:
                            break
                        
                        if graph[row][col] != -1 and graph[row][col] != 999:
                            graph[blank][col] = graph[row][col]
                            graph[row][col] = 999
                            
                            isFind = True
                            break
            
            if isFind == False:
                break


input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = []

res = 0

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    block_group = []
    max_block_cnt = 0
    max_rainbow_cnt = 0
    block_r, block_c = -1, -1
        
    for row in range(N):
        for col in range(N):
            if 0 < graph[row][col] <= M and visited[row][col] == 0:
                group, center_block, rainbow_block, rainbow_cnt = bfs(row, col)
                
                if len(group) < 2:
                    continue
                                
                if len(block_group) > 0:
                    if len(group) > max_block_cnt:
                        block_group.clear()
                        block_group.append(group)
                        max_block_cnt = len(group)
                        max_rainbow_cnt = rainbow_cnt
                    
                    elif len(group) == max_block_cnt:
                        if rainbow_cnt > max_rainbow_cnt:
                            block_group.clear()
                            block_group.append(group)
                            max_block_cnt = len(group)
                            max_rainbow_cnt = rainbow_cnt
                        
                        elif rainbow_cnt == max_rainbow_cnt:
                            if center_block[0] > block_r:
                                block_group.clear()
                                block_group.append(group)
                                max_block_cnt = len(group)
                                max_rainbow_cnt = rainbow_cnt
                            
                            elif center_block[0] == block_r:
                                if center_block[1] > block_c:
                                    block_group.clear()
                                    block_group.append(group)
                                    max_block_cnt = len(group)
                                    max_rainbow_cnt = rainbow_cnt
                    
                else:
                    block_group.append(group)
                    max_block_cnt = len(group)
                    max_rainbow_cnt = rainbow_cnt
                
                g = sorted(block_group[0], key=lambda x: (x[0], x[1]))
                block_r = g[0][0]
                block_c = g[0][1]
                
                if len(rainbow_block) > 0:
                    for r, c in rainbow_block:
                        visited[r][c] = 0
                
    
    if max_block_cnt < 2:
        break
    
    res += len(block_group[0]) ** 2
    
    for r, c in block_group[0]:
        graph[r][c] = 999
    
    gravity()
    
    graph = list(map(list, zip(*graph)))[::-1]
    
    gravity()

print(res)