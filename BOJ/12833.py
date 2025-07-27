A, B, C = map(int, input().split())

res = 0

if C % 2 == 0:
    res = A
else:
    res = A ^ B

print(res)