import sys


sys.setrecursionlimit(100000000)


def union(a, b):
    a_parent = find(a)
    b_parent = find(b)
    
    if a_parent < b_parent:
        rank[b_parent] = a_parent
    
    elif a_parent > b_parent:
        rank[a_parent] = b_parent


def find(node):
    if rank[node] != node:
        rank[node] = find(rank[node])
    
    return rank[node]


N, M = map(int, sys.stdin.readline().rstrip().split())

rank = [i for i in range(N + 1)]

for _ in range(M):
    operator, a, b = map(int, sys.stdin.readline().rstrip().split())
    
    if operator == 0:
        union(a, b)
    
    else:
        a_parent = find(a)
        b_parent = find(b)
        
        if a_parent == b_parent:
            print('YES')
        
        else:
            print('NO')