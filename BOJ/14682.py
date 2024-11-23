N = int(input())
K = int(input())

res = N

for _ in range(K):
    N *= 10
    res += N

print(res)