while True:
    n = int(input())

    if n == -1:
        break

    elapsed_t = 0
    res = 0

    for _ in range(n):
        s, t = map(int, input().split())

        res += s * (t - elapsed_t)
        elapsed_t = t

    print(f'{res} miles')