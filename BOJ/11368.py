while True:
    C, W, L, P = map(int, input().split())

    if C == W == L == P == 0:
        break

    res = C**(W * L * P)

    print(res)