from collections import defaultdict


N = int(input())

res = defaultdict(int)

for _ in range(N):
    line = input()

    res[len(line.split())] += 1

for key, value in sorted(res.items()):
    print(key, value)