x, y = map(int, input().split())

if x < y:
    print(abs(x - y))
else:
    print(x + y)