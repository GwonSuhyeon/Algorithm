T = int(input())

for _ in range(T):
    N = int(input())

    res = 999999
    cw = 999999

    for _ in range(N):
        W, C = map(int, input().split())

        if (C / W) < cw:
            cw = C / W
            res = C
        elif (C / W) == cw:
            res = min(res, C)
    
    print(res)