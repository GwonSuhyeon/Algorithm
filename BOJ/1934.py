import math

t = int(input())

res = []

for i in range(t):
    a, b = map(int, input().split())
    
    res.append(math.lcm(a, b))

for i in res:
    print(i)