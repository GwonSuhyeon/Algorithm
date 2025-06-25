T = int(input())

for _ in range(T):
    M, N = map(int, input().split())
    
    table = []
    res = 0
    maximum = 0
    
    for _ in range(N):
        table.append(list(map(int, input().split())))
    
    for column in range(M):
        temp = 1
        
        for row in range(N):
            temp *= table[row][column]
        
        if res == 0:
            maximum = temp
            res = 1
        else:
            if temp >= maximum:
                maximum = temp
                res = column + 1
    
    print(res)