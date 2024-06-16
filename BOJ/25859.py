from collections import defaultdict


S = input()

arr = defaultdict(int)

for i in S:
    arr[i] += 1

arr = sorted(arr.items(), key=lambda x : (-x[1], x[0]))

for key, value in arr:
    print(key * value, end='')