while True:
    x = float(input())

    if x == 0:
        break
    
    res = 0

    for i in range(0, 5):
        res += (x**i)
    
    print(f'{res:.2f}')