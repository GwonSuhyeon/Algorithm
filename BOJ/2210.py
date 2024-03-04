def dfs(row, col, arr):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    if len(arr) == 6:
        return
    
    for y, x in direction:
        new_row, new_col = row + y, col + x
        
        if new_row >= 0 and new_row < 5 and new_col >= 0 and new_col < 5:
            temp = arr + str(graph[new_row][new_col])
            
            if len(temp) == 6:
                res.append(temp)
            
            elif len(temp) < 6:
                dfs(new_row, new_col, temp)
            

graph = [[] for _ in range(5)]
res = []

for i in range(5):
    digit = input().split()
    
    for d in digit:
        graph[i].append(int(d))

for row in range(5):
    for col in range(5):
        dfs(row, col, str(graph[row][col]))

print(len(set(res)))