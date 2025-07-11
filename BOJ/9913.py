from collections import defaultdict


N = int(input())

arr = defaultdict(int)

for _ in range(N):
    n = int(input())
    
    arr[n] += 1

print(max(arr.values()))