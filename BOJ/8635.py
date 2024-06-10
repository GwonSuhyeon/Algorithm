from collections import defaultdict


N = int(input())

res = defaultdict(int)

for _ in range(N):
    S = input().split()
    
    S = ''.join(S)
    
    for i in S:
        if 'A' <= i <= 'Z':
            res[ord(i) + 1000] += 1
        
        else:
            res[ord(i)] += 1

res = sorted(res.items(), key=lambda x : x[0])

for key, value in res:
    if key >= 1000:
        print(chr(key - 1000), value)
    
    else:
        print(chr(key), value)