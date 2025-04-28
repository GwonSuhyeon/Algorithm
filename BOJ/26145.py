N, M = map(int, input().split())

S = list(map(int, input().split()))

res = [0 for _ in range(N + M)]

for idx, s in enumerate(S):
    res[idx] = s

for i in range(N):
    T = list(map(int, input().split()))

    for j, t in enumerate(T):
        res[i] -= t
        res[j] += t

print(*res)