n = int(input())

for _ in range(n):
    x = int(input())

    res = 0

    for _ in range(x):
        name, quantity, unit = input().split()

        quantity = int(quantity)
        unit = float(unit)

        res += quantity * unit
    
    print(f'${round(res, 2):.2f}')