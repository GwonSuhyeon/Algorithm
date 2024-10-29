n = int(input())

t, s = [], []

for _ in range(n):
    ti, si = map(int, input().split())

    t.append(ti)
    s.append(si)

k = max(s)

if k == 0:
    print(0)
    exit()

for i in range(0, len(s)):
    if s[i] == k:
        f = i + 1
        break

P = t[f - 1] + ((f - 1) * 20)

print(P)