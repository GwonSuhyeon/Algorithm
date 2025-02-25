button = list(map(int, input().split()))

res = 5000

for b in button:
    if b == 1:
        res -= 500
    elif b == 2:
        res -= 800
    else:
        res -= 1000

print(res)