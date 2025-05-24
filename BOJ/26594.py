from collections import defaultdict


s = input()

res = defaultdict(int)

for i in s:
    res[i] += 1

print(max(res.values()))