from collections import defaultdict


N = int(input())
S = input()

res = defaultdict(int)
hiarc = set(['H', 'I', 'A', 'R', 'C'])

for s in S:
    if s in hiarc:
        res[s] += 1

if len(res.keys()) < 5:
    print(0)
else:
    print(min(res.values()))