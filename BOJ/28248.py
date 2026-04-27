P = int(input())
C = int(input())

res = (P * 50) - (C * 10)

if P > C:
    res += 500

print(res)