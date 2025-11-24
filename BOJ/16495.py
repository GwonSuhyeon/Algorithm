S = input()

res = 0

for i in S:
    res *= 26
    res += (ord(i) - ord('A') + 1)

print(res)