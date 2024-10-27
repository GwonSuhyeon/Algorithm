import math


T = int(input())

golden_ratio = (1 + math.sqrt(5)) / 2
tolerance = (golden_ratio) * 0.01

for _ in range(T):
    a, b = map(float, input().split())

    if golden_ratio - tolerance <= (max(a, b) / min(a, b)) <= golden_ratio + tolerance:
        print('golden')
    else:
        print('not')