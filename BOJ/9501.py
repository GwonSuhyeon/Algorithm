T = int(input())

for _ in range(T):
    N, D = map(int, input().split())
    
    res = 0

    for _ in range(N):
        v, f, c = map(int, input().split())
        
        dist = (v / c) * f

        if dist >= D:
            res += 1
    
    print(res)