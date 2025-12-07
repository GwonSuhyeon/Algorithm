T = int(input())

for _ in range(T):
    value, c = input().split()
    value = float(value)

    if c == 'kg':
        print(f'{round(value * 2.2046, 4):.4f} lb')
    elif c == 'lb':
        print(f'{round(value * 0.4536, 4):.4f} kg')
    elif c == 'l':
        print(f'{round(value * 0.2642, 4):.4f} g')
    elif c == 'g':
        print(f'{round(value * 3.7854, 4):.4f} l')