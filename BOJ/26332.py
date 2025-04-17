n = int(input())

for _ in range(n):
    c, p = map(int, input().split())

    res = p

    if c > 1:
        res += (p - 2) * (c - 1)
    
    print(c, p)
    print(res)