N = int(input())

for i in range(1, N + 1):
    star = '*' * i

    print(star + (' ' * (2 * (N - i)) + star))

for i in range(N - 1, 0, -1):
    star = '*' * i

    print(star + (' ' * (2 * (N - i)) + star))