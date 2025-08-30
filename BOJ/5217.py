import math


T = int(input())

for _ in range(T):
    n = int(input())
    
    res = []
    
    for i in range(1, int(math.ceil(n / 2))):
        res.append([i, n - i])
    
    print(f'Pairs for {n}: ', end='')
    
    if len(res) == 0:
        print()
    else:
        for idx, (a, b) in enumerate(res):
            if (idx + 1) < len(res):
                print(f'{a} {b}, ', end='')
            else:
                print(f'{a} {b}')