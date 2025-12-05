T = int(input())

coins = [25, 10, 5, 1]

for _ in range(T):
    C = int(input())

    res = []

    for coin in coins:
        cnt = C // coin

        res.append(cnt)
        
        C %= coin
    
    print(*res)