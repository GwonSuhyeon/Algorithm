d1, d2, d3 = map(int, input().split())

a = (d1 + d2 - d3) / 2
c = d2 - a
b = d3 - c

if (a + b) == d1 and (a + c) == d2 and (b + c) == d3:
    if a > 0 and b > 0 and c > 0:
        print(1)
        print(a, b, c)
    else:
        print(-1)
else:
    print(-1)