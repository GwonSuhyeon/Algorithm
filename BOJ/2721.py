T = int(input())

Tn = []

for i in range(302):
    if i > 0:
        Tn.append(Tn[i - 1] + i)
    else:
        Tn.append(0)

for _ in range(T):
    n = int(input())

    res = 0

    for k in range(1, n + 1):
        res += (k * Tn[k + 1])
    
    print(res)