m, n = map(int, input().split())

prime = [1 for _ in range(1000000 + 1)]

for i in range(1000000 + 1):
    if i == 0:
        continue
    
    elif i == 1:
        prime[i] = 0
    
    else:
        if prime[i] == 1:
            for k in range(2 * i, 1000000 + 1, i):
                prime[k] = 0

for i in range(m, n + 1):
    if prime[i] == 1:
        print(i)