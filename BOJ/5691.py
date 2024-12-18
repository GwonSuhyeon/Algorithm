while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    
    c1 = 3 * a - a - b
    c2 = 3 * b - a - b
    c3 = (a + b) // 2

    print(min(c1, c2, c3))