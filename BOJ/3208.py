M, N = map(int, input().split())

if M > N:
    res = (2 * N) - 1
else:
    res = (2 * M) - 2

print(res)