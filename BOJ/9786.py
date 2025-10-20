import math


n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    gcd = math.gcd(a, b)

    print(a // gcd, b // gcd)