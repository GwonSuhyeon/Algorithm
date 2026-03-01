import math


w, h = map(int, input().split())

res = (w + h) - math.sqrt(w**2 + h**2)

print(res)