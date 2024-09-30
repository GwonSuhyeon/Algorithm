n = int(input())

for i in range(n):
    m = int(input())

    print(f'Case {i + 1}:')
    for _ in range(m):
        num = int(input())

        if (num + 1) <= 6:
            print(num + 1)