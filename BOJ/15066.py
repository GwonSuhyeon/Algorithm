import math


n = int(input())

res = 0

for _ in range(n):
    a, d = map(int, input().split())

    res += d * math.sin((a * math.pi) / 180.0)

print(f'{res:.2f}')