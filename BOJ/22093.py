T = int(input())

for _ in range(T):
    n, a, b = map(int, input().split())

    print(max(0, a - b), min(a, n - b))