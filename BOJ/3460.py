T = int(input())

for _ in range(T):
    n = int(input())

    res = ''
    
    while n > 0:
        res += str(n % 2)
        n //= 2
    
    for idx, i in enumerate(res):
        if i == '1':
            print(idx, end=' ')
    print()