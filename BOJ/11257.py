import math


N = int(input())

for _ in range(N):
    a, b, c, d = input().split()
    b = int(b)
    c = int(c)
    d = int(d)

    if b + c + d >= 55 and \
        b >= math.ceil(35 * 0.3) and \
        c >= math.ceil(25 * 0.3) and \
        d >= math.ceil(40 * 0.3):
        print(f"{a} {b + c + d} PASS")
    else:
        print(f"{a} {b + c + d} FAIL")