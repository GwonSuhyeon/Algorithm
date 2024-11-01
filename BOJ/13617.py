N, M = map(int, input().split())

res = 0

for _ in range(N):
    arr = list(map(int, input().split()))

    if 0 not in arr:
        res += 1

print(res)