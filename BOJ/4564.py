while True:
    S = input()

    if S == '0':
        break

    print(S, end=' ')

    while int(S) >= 10:
        res = 1

        for i in S:
            res *= int(i)
        
        print(res, end=' ')

        S = str(res)
    
    print()