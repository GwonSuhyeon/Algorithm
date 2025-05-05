A, B, digit = map(int, input().split())

res = 0

for i in range(A, B + 1):
    res += list(str(i)).count(str(digit))

print(res)