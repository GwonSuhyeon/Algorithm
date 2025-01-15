n = int(input())

S1 = input()
S2 = input()

res = 0

for s1, s2 in zip(S1, S2):
    if s1 != s2:
        res += 1

print(res)