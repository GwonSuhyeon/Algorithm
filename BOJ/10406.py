W, N, P = map(int, input().split())

P = list(map(int, input().split()))

res = 0

for p_i in P:
    if W <= p_i <= N:
        res += 1

print(res)