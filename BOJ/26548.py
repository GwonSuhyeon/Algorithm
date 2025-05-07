import math


n = int(input())

for _ in range(n):
    a, b, c = map(float, input().split())

    x1 = round((-b + math.sqrt(b**2 - (4 * a * c))) / (2 * a), 3)
    x2 = round((-b - math.sqrt(b**2 - (4 * a * c))) / (2 * a), 3)
    
    print(f'{x1:.3f}, {x2:.3f}')