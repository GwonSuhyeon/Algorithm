from collections import defaultdict


S = input()

res = defaultdict(int)

for i in S:
    res[i] += 1

keys = list(res.keys())

for i in range(ord('a'), ord('z') + 1):
    c = chr(i)
    
    if c in keys:
        print(res[c], end=' ')
    
    else:
        print(0, end=' ')