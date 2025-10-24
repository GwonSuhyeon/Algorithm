N, M = map(int, input().split())

arr = list(map(int, input().split()))

res = set()

for i in arr:
    for k in range(i, N + 1, i):
        if k not in res:
            res.add(k)

print(sum(res))