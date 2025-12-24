a, b = map(int, input().split())

width = b * (a % 2)
height = a * (b % 2)

res = min(width, height)

print(res)