p1, q1, p2, q2 = map(int, input().split())

res = (p1 * p2) % (q1 * q2 * 2)

if res == 0:
    print(1)
else:
    print(0)