A = input()
B = set(list(input()))

res = []

for a in A:
    if a in B:
        res.append(a.lower())
    else:
        res.append(a)

print(''.join(res))