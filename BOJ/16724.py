import sys
sys.setrecursionlimit(100000000)


def dfs(row, col):
    direction = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
    
    y, x = direction[graph[row][col]]
    
    new_row, new_col = row + y, col + x
    
    if visited[new_row][new_col] == 0:
        visited[new_row][new_col] += 1
        already = dfs(new_row, new_col)
        visited[new_row][new_col] += 1
        
        if already == True:
            return True
    
    elif visited[new_row][new_col] == 2:
        return True
    
    return False

input = sys.stdin.readline


N, M = map(int, input().rstrip().split())

graph = []

for _ in range(N):
    graph.append(list(input().rstrip()))

visited = [[0 for _ in range(M)] for _ in range(N)]

res = 0

for row in range(N):
    for col in range(M):
        if visited[row][col] == 0:
            visited[row][col] += 1
            if dfs(row, col) == False:
                res += 1
            visited[row][col] += 1

print(res)