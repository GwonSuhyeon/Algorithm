T = int(input())

for _ in range(T):
    price = float(input())

    print(f'${round(price - (price * 0.2), 3):.2f}')