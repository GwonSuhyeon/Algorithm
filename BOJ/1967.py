import sys


sys.setrecursionlimit(10000000)

def dfs(parent, current_node):
    
    temp = []
    
    visited[current_node] = 1
    
    if len(tree[current_node]) == 1:
        return 0
    
    for node, dist in tree[current_node]:
        if parent == node: continue
        
        d = dfs(current_node, node)
        
        if d > 0:
            temp.append(d + dist)
        
        else:
            temp.append(dist)
    
    if len(temp) > 0:
        first = max(temp)
        temp[temp.index(first)] = 0
        second = max(temp)
        
        node_dist[current_node] = (first + second)
        
        return first

N = int(input())

tree = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
node_dist = [0 for _ in range(N + 1)]

parent_node_list = []

for _ in range(N - 1):
    parent, child, dist = map(int, sys.stdin.readline().rstrip().split())
    
    tree[parent].append([child, dist])
    tree[child].append([parent, dist])
    
    parent_node_list.append(parent)

# dfs(0, 1)
for p in parent_node_list:
    if visited[p] == 0:
        dfs(0, p)

print(max(node_dist))