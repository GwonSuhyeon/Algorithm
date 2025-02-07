k, d = map(int, input().split())

res = 0
l = k
i = 0

while True:
    d -= k * (2**i)
    
    if d < 0:
        break
    else:
        res += 1
        i += 1

print(res)