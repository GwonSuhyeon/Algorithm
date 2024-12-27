T = int(input())

for _ in range(T):
    N = int(input())
    
    res = 0

    for i in range(1, N + 1):
        if i % 2 != 0:
            res += i
    
    print(res)