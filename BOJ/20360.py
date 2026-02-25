n = int(input())

res = []

while n > 0:
    if n % 2 == 0:
        res.append(0)
    else:
        res.append(n % 2)

    n //= 2

for idx, i in enumerate(res):
    if i == 1:
        print(idx, end=' ')