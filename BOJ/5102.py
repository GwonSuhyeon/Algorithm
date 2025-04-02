while True:
    a, b = map(int, input().split())
    
    pairs = 0
    groups = 0

    if a == 0 and b == 0:
        break

    if (a - b) < 3 or (a - b) % 2 == 0:
        pairs = (a - b) // 2
        groups = 0
    else:
        pairs = ((a - b) - 3) // 2
        groups = 1
    
    print(pairs, groups)