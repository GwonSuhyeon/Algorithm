from collections import defaultdict


S = input()

arr = defaultdict(int)

for i in S:
    if i in ['a', 'e', 'i', 'o', 'u']:
        arr[i] += 1

print(sum(arr.values()))