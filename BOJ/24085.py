from collections import defaultdict


N = int(input())
arr = list(map(int, input().split()))

count = defaultdict(int)

for i in arr:
    count[i] += 1

count = sorted(count.items(), key=lambda x : (x[1], x[0]))

print(count[0][0])