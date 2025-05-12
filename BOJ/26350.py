n = int(input())

for _ in range(n):
    coins = sorted(list(map(int, input().split()))[1:])
    
    res = True

    for i in range(len(coins) - 1):
        if coins[i + 1] < (coins[i] * 2):
            res = False
            
            break
    
    print('Denominations: ', end='')
    print(*coins)

    if res == True:
        print('Good coin denominations!', end='\n\n')
    else:
        print('Bad coin denominations!', end='\n\n')