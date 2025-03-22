N = int(input())
A, B = map(int, input().split())

res = A // 2 + B

if res <= N:
    print(res)
else:
    print(N)