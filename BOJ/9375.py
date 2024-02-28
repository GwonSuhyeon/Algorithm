from collections import defaultdict

t = int(input())

res = []

for _ in range(t):
    n = int(input())
    
    if n == 0:
        res.append(0)
        continue
    
    clothes = defaultdict(int)
    
    sum = 1
    
    for _ in range(n):
        s = input().split()
        
        clothes[s[1]] += 1
    
    for i in clothes.values():
        sum *= (i + 1)
    
    res.append(sum - 1)

for i in res:
    print(i)