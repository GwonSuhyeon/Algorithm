N, T, C, P = map(int, input().split())

res = ((N - 1) // T) * (C * P)

print(res)