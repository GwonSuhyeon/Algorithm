T = int(input())

for i in range(1, T + 1):
    num = int(input())

    print(f'Case {i}:')
    
    for k in range(1, 7):
        if k <= (num - k) <= 6:
            print(f'({k},{num - k})')