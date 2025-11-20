import math


n = int(input())
x1, y1 = map(int, input().split())

res = [0, 0, 999999]

for _ in range(n - 1):
    x2, y2 = map(int, input().split())

    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    if dist < res[-1]:
        res = [x2, y2, dist]

print(x1, y1)
print(res[0], res[1])
print(f'{res[-1]:.2f}')