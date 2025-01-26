n = int(input())

arr = list(map(int, input().split()))

res = [0 for _ in range(n)]
res[0] = 1

for idx, i in enumerate(arr):
    res[i + 1] = idx + 2

print(*res)