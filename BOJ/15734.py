L, R, A = map(int, input().split())

x = min(A, abs(L - R))

if L >= R:
    R += x
else:
    L += x

y = (A - x) // 2

res = 2 * min(L + y, R + y)

print(res)