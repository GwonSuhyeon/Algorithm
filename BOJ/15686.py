import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())

chicken = []
house = []

res = 99999

for i in range(N):
    s = input().split()
    
    for idx in range(len(s)):
        if int(s[idx]) == 2:
            chicken.append([i + 1, idx + 1])
        
        elif int(s[idx]) == 1:
            house.append([i + 1, idx + 1])

for c in combinations(chicken, M):
    total_dist = 0
    
    for h in house:
        dist = 99999
        
        for idx in range(M):
            house_y, house_x = h
            chicken_y, chicken_x = c[idx]
                        
            dist = min(dist, abs(house_x - chicken_x) + abs(house_y - chicken_y))
        
        total_dist += dist
    
    res = min(res, total_dist)

print(res)