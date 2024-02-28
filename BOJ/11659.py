n, m = map(int, input().split())
arr = input().split()

prefix_sum = [0 for _ in range(n + 1)]
res = []

for idx, i in enumerate(arr):
    prefix_sum[idx + 1] = prefix_sum[idx] + int(i)

for _ in range(m):
    i, j = map(int, input().split())
    
    res.append(prefix_sum[j] - prefix_sum[i - 1])

for i in res:
    print(i)