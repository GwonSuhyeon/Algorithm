n = int(input())

for _ in range(n):
    A1, P1 = map(int, input().split())
    R1, P2 = map(int, input().split())

    pizza1 = A1 / P1
    pizza2 = (R1**2 * 3.14) / P2

    if pizza1 > pizza2:
        print('Slice of pizza')
    else:
        print('Whole pizza')