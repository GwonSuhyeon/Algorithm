s1 = input()
s2 = input()

res = 1

for a, b in zip(s1, s2):
    if int(a) != int(b):
        res *= 2

print(res)