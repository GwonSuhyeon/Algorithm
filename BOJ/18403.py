T = int(input())

for _ in range(T):
    Y = list(map(int, input().split(', ')))
    
    res = []

    for y in Y:
        if y % 4 == 0:
            res.append(y)
    
    print(*res)