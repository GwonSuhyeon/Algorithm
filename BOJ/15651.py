def dfs():
    
    for i in range(1, N + 1):
        part.append(i)
        
        if len(part) == M:
            # res.append(part.copy())
            for i in part:
                print(i, end=' ')
            print()
        
        else:
            dfs()
        
        part.pop()

N, M = map(int, input().split())

arr = [i for i in range(N + 1)]
visited = [0 for _ in range(N + 1)]

# res = []
part = []

dfs()

# for i in res:
#     for k in i:
#         print(k, end=' ')
#     print()