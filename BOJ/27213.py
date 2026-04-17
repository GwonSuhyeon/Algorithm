m = int(input())
n = int(input())

res = 0

if m == 1 or n == 1:
    res = m * n
else:
    res = (m * n) - ((m - 2) * (n - 2))

print(res)