n = int(input())

res = {'a': 0, 'b': 0}

for _ in range(n):
    a, b = map(int, input().split())

    if a > b:
        res['a'] += (a + b)
    elif a < b:
        res['b'] += (a + b)
    else:
        res['a'] += a
        res['b'] += b

print(*res.values())