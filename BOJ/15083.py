p = sorted(list(map(int, input().split())), reverse=True)
c1, c2, c3 = map(int, input().split())

res1 = 0.01 * c1 * sum(p)
res2 = 0.01 * ((max(c2, c3) * p[0]) + (min(c2, c3) * p[1]))

if res1 > res2:
    print(f'one {res1:.2f}')
else:
    print(f'two {res2:.2f}')