T = int(input())

for _ in range(T):
    N = int(input())

    L_maximum = 0
    res = ""

    for _ in range(N):
        S, L = input().split()

        if int(L) > L_maximum:
            L_maximum = int(L)
            res = S
    
    print(res)