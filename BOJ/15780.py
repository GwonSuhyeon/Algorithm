N, K = map(int, input().split())
A = list(map(int, input().split()))

res = 0

for i in A:
    res += (i + 1) // 2

if res >= N:
    print('YES')
else:
    print('NO')