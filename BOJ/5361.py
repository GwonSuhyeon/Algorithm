T = int(input())

arr = [350.34, 230.90, 190.55, 125.30, 180.90]

for _ in range(T):
    A, B, C, D, E = map(int, input().split())

    res = arr[0] * A
    res += arr[1] * B
    res += arr[2] * C
    res += arr[3] * D
    res += arr[4] * E

    print(f'${res:.2f}')