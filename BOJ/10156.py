K, N, M = map(int, input().split())

num = M - (K * N)

if num < 0:
    print(abs(num))
else:
    print(0)