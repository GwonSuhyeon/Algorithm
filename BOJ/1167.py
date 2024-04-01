import sys


sys.setrecursionlimit(10000000)

def dfs(parent, current_node) -> int: # type: ignore
    
    temp = []
    
    visited[current_node] = 1

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
    
    else:
        return 0
    
V = int(input())

tree = [[] for _ in range(V + 1)]
visited = [0 for _ in range(V + 1)]
node_dist = [0 for _ in range(V + 1)]

parent_node_list = []

for _ in range(V):
    line = list(map(int, input().split()))
    
    for i in range(1, len(line), 2):
        if line[i] == -1: break
        tree[line[0]].append([line[i], line[i + 1]])
    
    parent_node_list.append(line[0])

for p in parent_node_list:
    if visited[p] == 0:
        dfs(0, p)

print(max(node_dist))