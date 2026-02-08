from collections import defaultdict


N = int(input())
S = input()

tmp = set(['a', 'e', 'i', 'o', 'u'])
arr = defaultdict(int)

for i in S:
    if i in tmp:
        arr[i] += 1

res = arr.values()

print(sum(res))