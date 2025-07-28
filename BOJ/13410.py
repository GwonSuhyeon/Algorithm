N, K = map(int, input().split())

res = 0

for i in range(1, K + 1):
    res = max(res, int(str(N * i)[::-1]))

print(res)