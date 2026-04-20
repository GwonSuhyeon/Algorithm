n, x, y = map(int, input().split())

for _ in range(n):
    a = int(input())

    res = (a * y) // x

    print(res)