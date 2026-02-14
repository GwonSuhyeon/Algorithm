from collections import defaultdict


N, M = map(int, input().split())
arr = list(map(int, input().split()))

res = defaultdict(int)

for i in arr:
    res[i] += 1

print(max(res.values()))