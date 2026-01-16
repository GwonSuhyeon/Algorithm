T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    res = (A // B)**2
    
    print(res)