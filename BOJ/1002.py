import math

t = int(input())

res = []

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
    if r1 + r2 == dist and r1 > 0 and r2 > 0:
        res.append(1)
    
    elif abs(r1 - r2) == dist and r1 != r2:
        res.append(1)
    
    elif r1 + r2 > dist and abs(r1 - r2) < dist:
        res.append(2)
    
    elif dist == 0 and r1 == r2:
        res.append(-1)
    
    else:
        res.append(0)

for i in res:
    print(i)