n = int(input())

for _ in range(n):
    p, t = map(int, input().split())

    res = p - (t // 7) + (t // 4)

    print(res)