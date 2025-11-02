n = int(input())

res = 0

for i in range(n // 2 + 1):
    if i <= 5 and (n - i) <= 5:
        res += 1

print(res)