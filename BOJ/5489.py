from collections import defaultdict


N = int(input())

arr = defaultdict(int)

for _ in range(N):
    arr[int(input())] += 1

res = min([key for key, value in arr.items() if value == max(arr.values())])

print(res)