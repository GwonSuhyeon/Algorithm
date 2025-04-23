g, p, t = map(int, input().split())

res1 = 0
res2 = 0

res1 = g * p
res2 = g + (p * t)

if res1 < res2:
    print(1)
elif res1 > res2:
    print(2)
else:
    print(0)