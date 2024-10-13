N = int(input())
P = int(input())

res = []

if N < 5:
    res.append(P)

if N >= 5:
    discount = 500

    if P < discount:
        res.append(0)
    else:
        res.append(P - discount)

if N >= 10:
    discount = int(P * 0.1)

    if P < discount:
        res.append(0)
    else:
        res.append(P - discount)

if N >= 15:
    discount = 2000

    if P < discount:
        res.append(0)
    else:
        res.append(P - discount)

if N >= 20:
    discount = int(P * 0.25)

    if P < discount:
        res.append(0)
    else:
        res.append(P - discount)

print(min(res))