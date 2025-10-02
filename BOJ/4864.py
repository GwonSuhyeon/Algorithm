while True:
    n = int(input())

    if n == 0:
        break
    
    res = 0
    k = 0
    day = 0

    while True:
        k += 1

        if day + k > n:
            break
        
        day += k
        res += k * k
    
    res += abs(day - n) * k
    
    print(n, res)