n = int(input())
m = int(input())

res = min(n, m) * 2

if abs(n - m) % 2 == 1:
    res += 1

print(res)