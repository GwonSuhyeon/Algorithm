n = int(input())

for _ in range(n):
    x = int(input())

    i = 10

    while x > i:
        x = int((x / i) + 0.5) * i

        i *= 10
    
    print(x)