n = int(input())

c1 = 0
c2 = 0

v1_sum = 0
v2_sum = 0

for _ in range(n):
    e, v1, v2 = map(int, input().split())

    if v1 > v2:
        c1 += e
    elif v1 < v2:
        c2 += e
    
    v1_sum += v1
    v2_sum += v2

if c1 > c2 and v1_sum > v2_sum:
    print(1)
elif c1 < c2 and v1_sum < v2_sum:
    print(2)
else:
    print(0)