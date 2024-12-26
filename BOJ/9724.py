import math

T = int(input())

for t in range(T):
    A, B = map(int, input().split())

    a = math.ceil(A**(1 / 3))
    b = math.floor(B**(1 / 3))

    res = max(0, b - a + 1)
    
    print(f'Case #{t + 1}: {res}')