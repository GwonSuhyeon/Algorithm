T = int(input())

for _ in range(T):
    E, N = map(int, input().split())

    res = 0

    for _ in range(N):
        num = int(input())

        if num > E:
            res += 1
    
    print(res)