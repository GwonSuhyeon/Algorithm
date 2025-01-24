N, T = map(int, input().split())

res = 0
up = True

for _ in range(T):
    if up == True:
        res += 1

        if res == (2 * N):
            up = False
    else:
        res -= 1
        
        if res == 1:
            up = True

print(res)