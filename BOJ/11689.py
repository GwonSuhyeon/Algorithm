import math


N = int(input())

res = N

for k in range(2, int(math.sqrt(N)) + 1):
    if (N % k) == 0:
        while (N % k) == 0:
            N //= k
        
        res *= (1 - (1 / k))

if N != 1:
    res *= (1 - (1 / N))

print(int(res))