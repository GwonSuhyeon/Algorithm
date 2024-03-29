from collections import deque


def bfs(start, end):
    
    bfs_q = deque()
    bfs_q.append([start, 0])
    visited[start] = 1
    
    while len(bfs_q):
        current_node, dist_sum = bfs_q.popleft()
        
        if current_node == end:
            return dist_sum
        
        for node, dist in tree[current_node]:
            if visited[node] == 0:
                bfs_q.append([node, dist_sum + dist])
                visited[node] = 1

N, M = map(int, input().split())

tree = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, dist = map(int, input().split())
    
    tree[a].append([b, dist])
    tree[b].append([a, dist])

for _ in range(M):
    start, end = map(int, input().split())
    
    visited = [0 for _ in range(N + 1)]
    
    dist_sum = bfs(start, end)
    
    print(dist_sum)